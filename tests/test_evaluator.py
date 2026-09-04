from unittest import TestCase
from unittest.mock import patch
from execution.stack import CallStack
from execution.evaluator import Evaluator

class TestEvaluator(TestCase):
    """ test the evaluator that calls other functions """
    
    # sample values. can be any but must be consistent
    VAL: str = " \t     \t" # capital a, 65, or 0b1000001
    PUSH_MANY_VAL: list[str] = ["push", VAL] * 2
    ASCII_VAL: int = 65
    STACK_VALS: list[int] = [ASCII_VAL] * 2

    def setUp(self):
        self.s = CallStack()
        self.ev = Evaluator(None, self.s, verbose=True)

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

    def test_input_character(self):
        """ test input_access=True """
        self.s.push(self.ASCII_VAL)
        self.ev.tokens = ["input character"]
        with patch("sys.stdin.readline", return_value=chr(self.ASCII_VAL)+"\n"):
            res = self.ev.evaluate()
        self.assertEqual(res, "")
        self.assertEqual(self.ev.heap.retrieve(self.ASCII_VAL), self.ASCII_VAL)

    def test_input_number(self):
        self.s.push(self.ASCII_VAL)
        self.ev.tokens = ["input number"]
        with patch("sys.stdin.readline", return_value=f"-{self.ASCII_VAL}\n"):
            res = self.ev.evaluate()
        self.assertEqual(res, "")
        self.assertEqual(self.ev.heap.retrieve(self.ASCII_VAL), -self.ASCII_VAL)

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

    def test_integer_div(self):
        for a, b, c in ((5, 2, 2), (5, -2, -2)):
            self.s.push_many([a, b])
            self.ev.tokens = ["div"]
            res = self.ev.evaluate()
            self.assertEqual(res, f"{c}")
            self.assertIn(c, self.s.peek_all())
