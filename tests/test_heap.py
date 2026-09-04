from unittest import TestCase
from execution import Heap, Evaluator
from errors.memory import AddressNotFoundError

from lexer.tokenizer import Tokenizer

class TestHeapRetrieval(TestCase):
    """ test heap storage and retrieval """

    ADDR = 0 # address
    VAL = 2 # value

    def setUp(self):
        self.h = Heap()

    def test_retrieval(self):
        self.h.store(self.ADDR, self.VAL)
        res = self.h.retrieve(self.ADDR)
        self.assertEqual(res, self.VAL)

    def test_retrieval_error(self):
        with self.assertRaises(AddressNotFoundError):
            self.h.retrieve(self.VAL)

    def test_eval_retrieve(self):
        lex = Tokenizer()
        lex.inp = (
            "\\32\\32\\32\\32\\n" # push 0
            "\\32\\32\\32\\t\\32\\n" # push 2
            "\\t\\t\\32" # store in heap
            "\\32\\32\\32\\32\\n" # push 0
            "\\t\\t\\t" # retrieve from heap
        )
        ev = Evaluator(self.h)
        ev.tokens = lex.tokenize()
        res = ev.consumed_eval()

        self.assertEqual(res, "")
        self.assertEqual(ev.stack.peek_all(), [self.VAL])
        self.assertEqual(self.h.heap_dict, {self.ADDR: self.VAL})
