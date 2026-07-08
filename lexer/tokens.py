""" defining the tokens that will lead to functionality """

from collections.abc import Iterable

def sort_tokens(tokens: Iterable) -> list:
    """ sort appropriately since re goes with shortest """
    return sorted(tokens, key=len, reverse=True)

TOKENS: dict[str, dict[str, str]] = {
    " ": { # imp space
        " ": "push",
        "\n": "duplicate",
        "\n\n": "pop"
    },
    "\t ": { # imp arithmetic
        "  ": "add",
        " \t": "sub",
        " \n": "mul",
        "\t ": "floordiv",
        "\t\t": "mod"
    }
}

# instruction modifier parameters
IMP_PATTERN = rf"^({'|'.join(sort_tokens(TOKENS.keys()))})"

OP_PATTERNS = { # operators
    key: rf"^({'|'.join(sort_tokens(TOKENS[key].keys()))})" # regex of values
    for key in sort_tokens(TOKENS.keys()) # regexes in imp
}