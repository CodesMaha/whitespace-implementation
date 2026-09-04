from unittest import TestCase

from execution import CallStack, Evaluator
from read import get_filepath

class FileLike:
    def __init__(self, text: str):
        self._text = text
    def read(self) -> str:
        return self._text

class TestEvalVerbosity(TestCase):
    """ test verbose=True and verbose=False """

    def setUp(self):
        self.s = CallStack()
        self.ev = Evaluator(self.s, None, verbose=True)

    def test_output_number(self):
        self.ev.tokens = ["push", "  ", "output number"]
        res = self.ev.evaluate()
        self.assertEqual(res, "pushed 0\n0")

    def test_swap(self):
        self.ev.tokens = ["push", "  ", "push", " \t", "swap"]
        res = self.ev.evaluate()
        self.assertEqual(res, "pushed 0\npushed 1\nswapped from 1 to 0")

    def test_argparse(self):
        res = get_filepath(["foo.ws"])
        self.assertEqual(res, "foo.ws")
