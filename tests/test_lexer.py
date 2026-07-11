from unittest import TestCase
from lexer.tokenizer import tokenize
from errors.lexer import EmptySyntaxError

class TestLexer(TestCase):
    ONLY_IMP = "\\32"
    INSTRUCTION = f"{ONLY_IMP*3}\\t\\n"

    def test_instruction(self):
        matched_tokens = tokenize(self.INSTRUCTION)
        self.assertEqual(matched_tokens, [" ", " ", " \t\n"])

    def test_only_imp(self):
        with self.assertRaises(EmptySyntaxError):
            tokenize(self.ONLY_IMP)