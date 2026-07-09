""" map tokens to functions """

# import statements
# parameter types
import lexer.custom_types as type

# operations
from execution.stack import CallStack
from operator import add, sub, mul, floordiv, mod
from sys import exit

from dataclasses import dataclass
from collections.abc import Callable, Iterable
from typing import Any

@dataclass
class Instruction:
    operator: Callable 
    operand_amt: int = 0 # how many stack items to pop, or
    operand_type: Any = None
    stack_access: bool = False # if access to stack (one more param)

def sort_tokens(tokens: Iterable) -> list:
    """ sort appropriately since re goes with shortest """
    return sorted(tokens, key=len, reverse=True)

OPERATIONS: dict[str, Instruction] = {
    "push": Instruction(CallStack.push, 0, type.Number, True),
    "pop": Instruction(CallStack.pop, stack_access=True),
    "duplicate": Instruction(CallStack.duplicate, stack_access=True),
    "copy": Instruction(CallStack.copy, 0, type.Number, True),
    "slide": Instruction(CallStack.slide, 0, type.Number, stack_access=True),
    "swap": Instruction(CallStack.swap, stack_access=True),
    "add": Instruction(add, 2),
    "sub": Instruction(sub, 2),
    "mul": Instruction(mul, 2),
    "floordiv": Instruction(floordiv, 2),
    "mod": Instruction(mod, 2),
    "exit": Instruction(exit)
}