""" read input to render it useful """

from lexer.tokens import IMP_PATTERN, OP_PATTERNS
from errors.lexer import EmptySyntaxError

from re import sub, match

class Lexer:
    def __init__(self):
        self.inp = ""
        self.pos: int = 0

    @property
    def inp(self) -> str:
        return self._inp
    @inp.setter
    def inp(self, new_inp: str) -> None:
        # keep backslash and add \20 for convenience
        self._inp = new_inp.encode("latin1").decode("unicode_escape").replace("\32", " ")
        self._inp = sub(r"[^ \t\n]", "", self._inp) # keep only spaces, tabs, and newlines

    def analyze(self) -> list[str]:
        """ tokenize input then return matched_tokens """
        matched_tokens: list = [] # to append to

        m = match(IMP_PATTERN, self._inp)
        if not m:
            raise EmptySyntaxError
        matched_tokens.append(m.group(0))
        self.pos = len(matched_tokens[0])

        try:
            m = match(OP_PATTERNS[matched_tokens[0]], self._inp[self.pos:])
        except KeyError as exc:
            raise EmptySyntaxError(f"Unrecognized IMP used: {matched_tokens[0]!r}.") from exc
        
        if not m:
            raise EmptySyntaxError
        matched_tokens.append(m.group(0))
        self.pos += len(matched_tokens[1])

        # store rest of inp if parameter present
        matched_tokens.append(self._inp[self.pos:])

        return matched_tokens