import argparse
from collections.abc import Iterable
from typing import TextIO
from sys import argv

from lexer.tokenizer import Tokenizer
from execution import Evaluator
from config import VERBOSE_FILE

def get_filepath(args: Iterable[str]) -> str:
    """ use argparse to read args with .filepath """

    parser = argparse.ArgumentParser(
        prog="Whitespace interpreter",
        description="Interpret Whitespace code with the help of Python."
    )

    parser.add_argument(
        "filepath", help="filepath to the file to interpret"
    )
    args = parser.parse_args(args)
    return args.filepath

def read_filepath(*, fp: str = "", file: TextIO = None) -> str:
    """ read from filepath or file-like object """
    
    lex = Tokenizer()
    ev = Evaluator(verbose=VERBOSE_FILE)

    if fp:
        with open(fp, "r") as f:
            lex.inp = f.read()
    elif file:
        lex.inp = file.read()

    ev.tokens = lex.tokenize()
    return ev.evaluate()

if __name__ == "__main__":
    print(read_filepath(fp=get_filepath(argv[1:])))
