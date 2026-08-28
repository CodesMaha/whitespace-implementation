from typing import Any

class WhitespaceError(Exception):
    """ base custom program-specific error class """
    def __init__(self, message="Custom error occurred during runtime"):
        # no periods at the end when writing error messages
        self.message = message
        super().__init__(self.message)

def with_info(message: str, info: Any):
    """ return msg with info if info else msg """
    if info:
        return f"{message}: {info}"
    else:
        return message
