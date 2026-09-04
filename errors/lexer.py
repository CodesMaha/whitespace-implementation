""" errors that can be raised during lexical analysis """

from errors import WhitespaceError

class MissingSyntaxError(WhitespaceError):
    def __init__(
        self, message="Token matches not found when analyzing code",
        char_no: int | None = None
    ):
        if char_no is not None:
            message = f"{message} after whitespace character {char_no}"
        super().__init__(message)

class NumberError(WhitespaceError):
    def __init__(self, message="Invalid format for a number"):
        super().__init__(message)

class CharacterError(WhitespaceError):
    def __init__(self, message="Invalid format for a character"):
        super().__init__(message)

class UserNumberError(WhitespaceError):
    def __init__(self, message="Invalid numeric input from user"):
        super().__init__(message)
