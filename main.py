from lexer.lexer import Lexer
from execution.stack import CallStack
from execution.evaluator import evaluate_tokens

from sys import stdin

print("WHITESPACE") # title

# initialize
l = Lexer()
s = CallStack()
SENTINEL = "-1\n"

# main loop
while True:
    
    inp_lines = []
    print("$", end=" ") # symbol for accepting inp

    # loop for multiline inp
    while True:
        inp_line = stdin.readline()
        # check for sentinel value or eof condition
        if inp_line in ["", SENTINEL]:
            break 

        inp_lines.append(inp_line)

    l.inp = "".join(inp_lines)[:-1] # remove trailing newline
    print(f"{evaluate_tokens(l.analyze(), s)}")