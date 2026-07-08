""" errors that can be raised during lexical analysis """

class EmptySyntaxError(Exception):
    def __init__(self, message="Token matches not found when analyzing code."):
        self.message = message
        super().__init__(self.message)

class NumberError(Exception):
    def __init__(self, message="Invalid format for a number."):
        self.message = message
        super().__init__(self.message)