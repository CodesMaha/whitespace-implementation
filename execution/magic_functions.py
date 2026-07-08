""" called with tokens inputted """

from errors.lexer import NumberError

from re import sub as substitute, match
from operator import add, sub, mul, floordiv, mod
from sys import exit

class Number:
    def __init__(self, gvn_number: str):
        self.pattern = r"[ \t]+\n" # this newline has to be removed
        self._number: str | int = gvn_number
    
    @property
    def value(self): # must be value or consistent across types
        if not match(self.pattern, self._number):
            raise NumberError(f'Cannot convert {self._number!r} into usable number.')
        
        _number = substitute("\t", "1", substitute(" ", "0", self._number))[:-1] # convert to zeros and ones
        
        if len(_number) < 2: # after newline is removed
            raise NumberError
        
        if int(_number[0]) == 1:
            _number = -int(_number[1:], 2)
        else:
            _number = int(_number[1:], 2)
        return _number
        
    @value.setter
    def value(self, new_number):
        self._number = new_number