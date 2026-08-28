import argparse
from collections.abc import Iterable
from sys import argv

from lexer.tokenizer import Tokenizer
from execution.stack import CallStack
from execution.evaluator import Evaluator
from config import VERBOSE_FILE

def get_filepath(args: Iterable[str]) -> str:
    parser = argparse.ArgumentParser(
        prog="Whitespace interpreter",
        description="Interpret Whitespace code with the help of Python."
    )

    parser.add_argument(
        "filepath", help="filepath to the file to interpret"
    )
    args = parser.parse_args(args)
    return args.filepath

def read_filepath(*, fp: str = "", file = None) -> str:
    lex = Tokenizer()
    s = CallStack()
    ev = Evaluator(s, verbose=VERBOSE_FILE)

    if fp:
        with open(fp, "r") as f:
            lex.inp = f.read()
    elif file:
        lex.inp = file.read()

    ev.tokens = lex.tokenize()
    return ev.evaluate()

if __name__ == "__main__":
    print(read_filepath(fp=get_filepath(argv[1:])))
