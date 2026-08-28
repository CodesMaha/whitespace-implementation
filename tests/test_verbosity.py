from unittest import TestCase
from execution.stack import CallStack
from execution.evaluator import Evaluator

class TestEvalVerbosity(TestCase):
    def setUp(self):
        self.s = CallStack()
        self.ev = Evaluator(self.s, verbose=True)

    def test_output_number(self):
        self.ev.tokens = ["push", "  ", "output number"]
        res = self.ev.evaluate()
        self.assertEqual(res, "pushed 0\n0")

    def test_swap(self):
        self.ev.tokens = ["push", "  ", "push", " \t", "swap"]
        res = self.ev.evaluate()
        self.assertEqual(res, "pushed 0\npushed 1\nswapped from 1 to 0")
