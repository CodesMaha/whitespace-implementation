from unittest import TestCase
from execution.stack import CallStack
from execution.evaluator import evaluate_tokens

class TestEvaluator(TestCase):
    """ test the function that calls other functions """
    # sample values. can be any but must be consistent
    VAL: int = 65 # capital a
    VALS: list[int] = [VAL]*2

    def setUp(self):
        self.s = CallStack()

    def test_output_character(self):
        self.s.push(self.VAL)
        res = evaluate_tokens(["\t\n", "  "], self.s)
        self.assertEqual(res, chr(self.VAL))

    def test_output_number(self):
        self.s.push(self.VAL)
        res = evaluate_tokens(["\t\n", " \t"], self.s)
        self.assertEqual(res, self.VAL)

    def test_add(self):
        self.s.push_many(self.VALS)
        res = evaluate_tokens(["\t ", "  "], self.s) 
        self.assertEqual(res, sum(self.VALS)) 

    def test_mod(self):
        self.s.push_many(self.VALS)
        res = evaluate_tokens(["\t ", "\t\t"], self.s)
        self.assertEqual(res, 0)

        self.s.push_many([0, self.VAL])
        with self.assertRaises(ZeroDivisionError):
            evaluate_tokens(["\t ", "\t\t"], self.s)