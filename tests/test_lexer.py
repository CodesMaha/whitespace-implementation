from unittest import TestCase
from lexer.tokenizer import Tokenizer
from errors.lexer import MissingSyntaxError

class TestLexer(TestCase):
    ONLY_IMP = "\\32"
    INSTRUCTION = f"{ONLY_IMP*3}\\t\\n"

    def setUp(self):
        self.tokenizer = Tokenizer()

    def test_instruction(self):
        self.tokenizer.inp = self.INSTRUCTION
        matched_tokens = self.tokenizer.tokenize()
        self.assertEqual(matched_tokens, ["push", 1])

    def test_instructions(self):
        self.tokenizer.inp = self.INSTRUCTION * 2
        matched_tokens = self.tokenizer.tokenize()
        self.assertEqual(matched_tokens, ["push", 1] * 2)

    def test_only_imp(self):
        with self.assertRaises(MissingSyntaxError):
            self.tokenizer.inp = self.ONLY_IMP
            self.tokenizer.tokenize()