""" input and output types """

from errors.lexer import NumberError, CharacterError

from re import sub as substitute, fullmatch

class Number:
    # this pattern is for gvn_number but is apparent when getting
    pattern = r"^[ \t]+\n$" # this newline has to be removed while processing

    def __init__(self, gvn_number: str):
        self._number: str = gvn_number
    
    @property
    def value(self): # must be value or consistent across types
        if not fullmatch(self.pattern, self._number):
            raise NumberError(f'Cannot convert {self._number!r} into usable number.')
        
        # convert spaces to zeros and tabs to ones
        number: int | str = substitute("\t", "1", substitute(" ", "0", self._number))[:-1]
        
        if len(number) < 2: # after newline is removed
            raise NumberError
        
        if number[0] == "1":
            number = -int(number[1:], 2)
        else:
            number = int(number[1:], 2)
        return number
        
    @value.setter # error not raised here but in getting
    def value(self, new_number: str):
        self._number = new_number 

class Character:
    limit_7bit = 127 # 7-bit ascii

    def __init__(self, ascii_code: str):
        self._character: str = ascii_code
    
    @property
    def value(self): 
        character = Number(self._character).value

        # ensure clamping to range from 0 to self.limit_7b
        if self.limit_7bit < character < 0:
            raise CharacterError(f"Character can only be converted from an ASCII code. Number inputted: {self._character}.")
        
        return ascii(character)
    
    @value.setter
    def value(self, new_ascii_code: str):
        self._character = new_ascii_code