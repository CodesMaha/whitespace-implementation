""" errors that might be raised during stack manipulation """

from errors import WhitespaceError, with_info

class EmptyStackError(WhitespaceError):
    def __init__(self, message="Cannot perform operation due to no stack items"):
        super().__init__(message)

class MissingStackError(WhitespaceError):
    def __init__(
        self, message="Cannot perform operation due to insufficient stack size",
        size: int | str = 0
    ):
        super().__init__(with_info(message, size))

class PopZeroError(WhitespaceError):
    def __init__(self, message="Cannot pop zero or less times"):
        super().__init__(message)
