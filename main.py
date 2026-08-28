from lexer.tokenizer import Tokenizer
from execution.stack import CallStack
from execution.evaluator import Evaluator

from sys import stdin

SENTINEL = "-1\n"

def get_input() -> list[str]:
    """ get multiline input """
    inp_lines = []
    print("$", end=" ") # symbol for accepting inp

    while True:
        inp_line = stdin.readline()
        # check for sentinel value or eof condition
        if inp_line in ["", SENTINEL]:
            break 

        inp_lines.append(inp_line)
    
    return inp_lines

def main():
    print("WHITESPACE") # title

    # initialize
    lex = Tokenizer()
    s = CallStack()
    ev = Evaluator(stack=s)

    # main loop
    while True:
        inp_lines = get_input()
        lex.inp = "".join(inp_lines)[:-1]
        ev.tokens = lex.tokenize()
        print(ev.evaluate())

if __name__ == "__main__":
    main()