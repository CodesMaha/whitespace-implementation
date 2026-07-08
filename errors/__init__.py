class BaseRunningError(Exception):
    def __init__(self, message="Custom error occurred during runtime."):
        self.message = message
        super().__init__(self.message)