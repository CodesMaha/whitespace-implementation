

from unittest import TestCase
from lexer.tokenizer import Tokenizer
from execution import Evaluator

class TestEvaluator(TestCase):
    """ test the evaluator that calls other functions """

    def setUp(self):
        self.lex = Tokenizer()
        self.ev = Evaluator()

    def test_count(self):
        self.lex.inp = (
            "\32\32\32\t\n" # push 1
            "\n\32\32\32\t\32\32\32\t\t\n" # mark label start
            "\32\n\32" # duplicate
            "\t\n\32\t" # output number
            "\32\32\32\t\32\t\32\n" # push 10
            "\t\n\32\32" # output character
            "\32\32\32\t\n" # push 1
            "\t\32\32\32" # add
            "\32\n\32" # duplicate
            "\32\32\32\32\t\32\t\t\n" # push 11
            "\t\32\32\t" # subtract
            "\n\t\32\32\t\32\32\32\t\32\t\n" # jump if zero end
            "\n\32\n\32\t\32\32\32\t\t\n" # jump start
            "\n\32\32\32\t\32\32\32\t\32\t\n" # mark label end
            "\32\n\n" # pop
            "\n\n\n" # exit
        )
        self.ev.tokens = self.lex.tokenize()
        res = self.ev.consumed_eval()
        self.assertEqual(res, "".join(f"{i}\n" for i in range(1, 11)))

    def test_output_square(self):
        self.lex.inp = (
            "\32\32\32\t\32\n" # push 2
            "\n\32\32\n" # mark label
            "\32\n\32" # duplicate
            "\t\32\32\n" # multiply
            "\t\n\32\t" # output number
            "\32\32\32\t\32\t\32\n" # push 10
            "\t\n\32\32" # output character
            "\n\t\n" # end subroutine
            "\32\32\32\t\t\n" # push 3
            "\n\32\t\n" # call subroutine
        )
        self.ev.tokens = self.lex.tokenize()
        res = self.ev.consumed_eval()
        self.assertEqual(res, "4\n9\n")
