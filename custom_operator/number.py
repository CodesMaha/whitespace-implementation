""" input and output types """

from errors.lexer import NumberError, CharacterError

from re import fullmatch

NUMBER_PATTERN = r"[ \t]*" # for numbers
LIMIT_7BIT = 127 # for 7-bit ascii characters

def to_number(inp: str) -> int:
    """ parse parameter into usable Number 
    where default pushing i.e. storage is for any Number
    """
    if fullmatch(NUMBER_PATTERN, inp) is None:
        raise NumberError(f'Cannot convert {inp!r} into usable number')

    # convert spaces to zeros and tabs to ones
    res: int | str = inp.replace(" ", "0").replace("\t", "1")
    
    if len(res) < 2: # newline should be removed beforehand
        raise NumberError # has to contain sign and one digit
    
    if res[0] == "1":
        res = -int(res[1:], 2)
    else:
        res = int(res[1:], 2)
    return res

def integer_div(a: int, b: int) -> int:
    """ division concerning truncated floats """
    return int(a / b)

def to_character(inp: int) -> str:
    """ convert Number to Character """
    # ensure clamping to range from 0 to self.limit_7b
    if not is_7bit_ascii(inp):
        raise CharacterError(
            "Character can only be converted from an ASCII code. "
            f"Number inputted: {inp}"
        )
    
    return chr(inp)

def is_7bit_ascii(inp: int) -> bool:
    return 0 <= inp <= LIMIT_7BIT
