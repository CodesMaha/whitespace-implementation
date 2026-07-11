from unittest import TestCase
from execution.stack import CallStack
from execution.evaluator import evaluate_tokens

class TestEvaluator(TestCase):
    """ test the function that calls other functions """
    # sample values. can be any but must be consistent
    VAL: int = 65 # capital a or 0b1000001
    VALS: list[int] = [VAL]*2

    def setUp(self):
        self.s = CallStack()

    def test_stack_duplicate(self):
        """ test stack_access=True """
        self.s.push(self.VAL)
        evaluate_tokens([" ", "\n"], self.s)
        self.assertEqual(self.s.peek_all(), self.VALS)

    def test_output_character(self):
        """ test return_type=Truthy """
        self.s.push(self.VAL)
        res = evaluate_tokens(["\t\n", "  "], self.s)
        self.assertEqual(res, chr(self.VAL))
        self.assertEqual(self.s.peek_all(), [])

    def test_output_number(self):
        self.s.push(self.VAL)
        res = evaluate_tokens(["\t\n", " \t"], self.s)
        self.assertEqual(res, self.VAL)
        self.assertEqual(self.s.peek_all(), [])

    def test_add(self):
        """ test parameter_amt=Truthy """
        self.s.push_many(self.VALS)
        res = evaluate_tokens(["\t ", "  "], self.s) 
        self.assertEqual(res, sum(self.VALS)) 
        self.assertEqual(self.s.peek_all(), [sum(self.VALS)])

    def test_mod(self):
        self.s.push_many(self.VALS)
        res = evaluate_tokens(["\t ", "\t\t"], self.s)
        self.assertEqual(res, 0)
        self.assertEqual(self.s.peek_all(), [0])

        self.s.push_many([0, self.VAL])
        with self.assertRaises(ZeroDivisionError):
            evaluate_tokens(["\t ", "\t\t"], self.s)