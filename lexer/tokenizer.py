""" read input to render it useful """

from lexer.tokens import IMP_PATTERN, OP_PATTERNS, TOKENS
from execution.parser import OPERATIONS # to check if conversion
from errors.lexer import MissingSyntaxError

from re import sub, match as re_match

class Tokenizer:
    """ init tokenizer then tokenize """
    def __init__(self):
        self.inp = ""

    @property
    def inp(self) -> str:
        """ get and set curr inp; default empty str """
        return self._inp
    @inp.setter
    def inp(self, new_inp: str) -> None:
        self._inp = new_inp.encode("latin1").decode("unicode_escape")
        # keep only spaces, tabs, and newlines
        self._inp = sub(r"[^ \t\n]", "", self._inp.replace("\32", " "))

        self.pos: int = 0
        self.inp_len: int = len(self._inp)
        self.matched_tokens: list[str | int] = []

    def _update_tokens(self, new_match) -> None:
        """ update matched_tokens with new_match """
        self.matched_tokens.append(new_match)
    def _get_top(self) -> str | int:
        """ get top token from matched_tokens """
        try:
            return self.matched_tokens[-1]
        except IndexError:
            return ""
    
    def _update_pos(self, gvn_incr: int = 0) -> None:
        """ update from get_top len, or gvn_incr """
        self.pos += gvn_incr
    def _next(self) -> str:
        """ inp after pos """
        return self.inp[self.pos:]

    def tokenize(self) -> list[str]:
        """ tokenize curr inp then return matched_tokens """
        if self.pos == self.inp_len: # return at end of inp
            return self.matched_tokens

        m = re_match(IMP_PATTERN, self._next())
        if not m: raise MissingSyntaxError(char_no=self.pos)

        imp: str = m.group(0)
        self._update_pos(len(imp))

        try:
            m = re_match(OP_PATTERNS[imp], self._next())
        except KeyError as exc:
            raise MissingSyntaxError(
                f"Unrecognized IMP used: {imp!r}"
            ) from exc
        if not m: raise MissingSyntaxError(char_no=self.pos)

        self._update_tokens(TOKENS[imp][m.group(0)])
        self._update_pos(len(m.group(0)))

        if OPERATIONS[self._get_top()].parameter_type:
            # get until next newline
            gvn_number = self._next().split("\n", 1)[0]
            self._update_tokens(gvn_number) # no conversion
            self._update_pos(len(gvn_number) + 1)

        return self.tokenize()