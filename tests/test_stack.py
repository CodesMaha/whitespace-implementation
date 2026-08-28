from unittest import TestCase
from execution.stack import CallStack

class TestStackManipulation(TestCase):
    """ test stack manipulation imp such as for push """
    
    # these are sample values. they can change but should be consistent
    VAL: int = 65 # capital a for testing, but can be any int
    VALS: list[int] = [VAL, VAL+1, VAL] # alternating

    def setUp(self):
        self.s = CallStack()

    def test_peek(self):
        self.s.push(self.VAL)
        self.assertEqual(self.s.peek(), self.VAL)
    
    def test_pop(self):
        self.s.push(self.VAL)
        self.s.pop()
        self.assertEqual(self.s.peek_all(), [])

    def test_duplicate(self):
        self.s.push(self.VAL)
        self.s.duplicate()
        self.assertEqual(self.s.peek_all(), [self.VAL]*2)

    def test_copy(self):
        self.s.push_many(self.VALS[:2])
        self.s.copy(1)
        self.assertEqual(self.s.peek_all(), self.VALS)

    def test_swap(self):
        self.s.push_many(self.VALS[:2])
        self.s.swap()
        self.assertEqual(self.s.peek_all(), self.VALS[:2])

    def test_slide(self):
        self.s.push_many(self.VALS)
        # sub one for zero-indexed and one for top
        self.s.slide(len(self.VALS)-2)
        self.assertEqual(self.s.peek_all(), [self.VAL])
