from lexer.lexer import Lexer
from execution.stack import CallStack
from execution.evaluator import evaluate_tokens

print("WHITESPACE")

# initialize
inp = ""
l = Lexer()

s = CallStack()

# main loop
while True:
    inp = input("$ ")
    l.inp = inp
    print(f"{evaluate_tokens(l.analyze(), s)}")