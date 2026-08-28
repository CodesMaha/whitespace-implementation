import argparse

from lexer.tokenizer import Tokenizer
from execution.stack import CallStack
from execution.evaluator import Evaluator
from config import VERBOSE_FILE

parser = argparse.ArgumentParser(
    prog="Whitespace interpreter",
    description="Interpret Whitespace code with the help of Python."
)

parser.add_argument("filepath")
args = parser.parse_args()

lex = Tokenizer()
s = CallStack()
ev = Evaluator(s, verbose=VERBOSE_FILE)

with open(args.filename, "r") as f:
    lex.inp = f.read()
    ev.tokens = lex.tokenize()
    print(ev.evaluate())
