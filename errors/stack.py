""" errors that might be raised during stack manipulation """

from errors import BaseRunningError

class EmptyStackError(BaseRunningError):
    def __init__(self, message="Cannot perform operation due to no stack items found."):
        super().__init__(message)

class MissingStackError(BaseRunningError):
    def __init__(self, message="Cannot perform operation due to insufficient stack size."):
        super().__init__(message)

class PopZeroError(BaseRunningError):
    def __init__(self, message="Cannot pop zero or less times."):
        super().__init__(message)