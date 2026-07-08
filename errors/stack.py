""" errors that might be raised during stack manipulation """

from errors import BaseRunningError

class EmptyStackError(BaseRunningError):
    def __init__(self, message="Cannot perform operation due to insufficient stack size."):
        self.message = message
        super().__init__(self.message)

class ZeroPopError(BaseRunningError):
    def __init__(self, message="Number of times stack is popped cannot be less than zero."):
        self.message = message
        super().__init__(self.message)