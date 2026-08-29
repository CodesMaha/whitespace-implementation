""" errors that might be raised during stack manipulation """

from errors import WhitespaceError, with_info

#   stack errors

class EmptyStackError(WhitespaceError):
    def __init__(self, message="Operation not possible due to no stack items"):
        super().__init__(message)

class MissingStackError(WhitespaceError):
    def __init__(
        self, message="Cannot perform operation due to stack size",
        size: int | str = 0
    ):
        super().__init__(with_info(message, size))

class PopZeroError(WhitespaceError):
    def __init__(
        self, message="Stack size does not allow popping",
        idx_to_pop: int | None = None
    ):
        if idx_to_pop is not None:
            message = f"{message} item {idx_to_pop}"
        super().__init__(message)

#   heap errors

class AddressNotFoundError(WhitespaceError):
    def __init__(
        self, message="Could not find address to retrieve from",
        address: int | None = None
    ):
        if address is not None:
            message = f"{message}: {address}"
        super().__init__(message)
