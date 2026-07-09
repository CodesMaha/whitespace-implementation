""" errors that can be raised during lexical analysis """

from errors import BaseRunningError

class EmptySyntaxError(BaseRunningError):
    def __init__(self, message="Token matches not found when analyzing code."):
        super().__init__(message)

class NumberError(BaseRunningError):
    def __init__(self, message="Invalid format for a number."):
        super().__init__(message)

class CharacterError(BaseRunningError):
    def __init__(self, message="Invalid format for a character."):
        super().__init__(message)