""" read input to render it useful """

from lexer.tokens import IMP_PATTERN, OP_PATTERNS
from errors.lexer import EmptySyntaxError

from re import sub, match

def tokenize(inp: str) -> list[str]:
    """ tokenize input then return matched_tokens """
    inp = inp.encode("latin1").decode("unicode_escape").replace("\32", " ")
    inp = sub(r"[^ \t\n]", "", inp) # keep only spaces, tabs, and newlines

    matched_tokens: list = [] # to append to

    m = match(IMP_PATTERN,inp)
    if not m:
        raise EmptySyntaxError
    matched_tokens.append(m.group(0))
    pos = len(matched_tokens[0])

    try:
        m = match(OP_PATTERNS[matched_tokens[0]], inp[pos:])
    except KeyError as exc:
        raise EmptySyntaxError(f"Unrecognized IMP used: {matched_tokens[0]!r}.") from exc
    
    if not m:
        raise EmptySyntaxError
    matched_tokens.append(m.group(0))
    pos += len(matched_tokens[1])

    # store rest of inp if parameter present
    matched_tokens.append(inp[pos:])

    return matched_tokens