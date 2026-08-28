from unittest import TestCase
from execution.stack import CallStack
from execution.evaluator import Evaluator

class TestEvaluator(TestCase):
    """ test the function that calls other functions """
    # sample values. can be any but must be consistent
    VAL: str = " \t     \t" # capital a, 65, or 0b1000001
    PUSH_MANY_VAL: list[str] = ["push", VAL] * 2
    ASCII_VAL: int = 65
    STACK_VALS: list[int] = [ASCII_VAL] * 2

    def setUp(self):
        self.s = CallStack()
        self.ev = Evaluator(self.s)

    def test_stack_duplicate(self):
        """ test stack_access=True """
        self.ev.tokens = self.PUSH_MANY_VAL
        self.ev.evaluate()
        self.assertEqual(self.s.peek_all(), self.STACK_VALS)

    def test_output_character(self):
        """ test return_type=Truthy """
        self.s.push(self.ASCII_VAL)
        self.ev.tokens = ["output character"]
        res = self.ev.evaluate()
        self.assertEqual(res, chr(self.ASCII_VAL))
        self.assertEqual(self.s.peek_all(), [])

    def test_output_number(self):
        self.s.push(self.ASCII_VAL)
        self.ev.tokens = ["output number"]
        res = self.ev.evaluate()
        self.assertEqual(res, repr(self.ASCII_VAL))
        self.assertEqual(self.s.peek_all(), [])

    def test_add(self):
        """ test parameter_amt=Truthy """
        self.s.push_many(self.STACK_VALS)
        self.ev.tokens = ["add"]
        res = self.ev.evaluate()
        self.assertEqual(res, repr(sum(self.STACK_VALS))) 
        self.assertEqual(self.s.peek_all(), [sum(self.STACK_VALS)])

    def test_mod(self):
        self.s.push_many(self.STACK_VALS)
        self.ev.tokens = ["mod"]
        res = self.ev.evaluate()
        self.assertEqual(res, "0")
        self.assertEqual(self.s.peek_all(), [0])

        self.ev.tokens = ["push", self.VAL, "push", "  ", "mod"]
        with self.assertRaises(ZeroDivisionError):
            self.ev.evaluate()
