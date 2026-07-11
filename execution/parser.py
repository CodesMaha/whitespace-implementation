""" map tokens to functions """

# import statements
# parameter types
import lexer.to_type as type

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
    parameter_amt: int = 0 # how many stack items to pop
    parameter_type: Any = None
    return_type: Any = None
    store_return: bool = False # push to stack
    stack_access: bool = False # if access to stack (one more param)

def sort_tokens(tokens: Iterable) -> list:
    """ sort appropriately since re goes with shortest """
    return sorted(tokens, key=len, reverse=True)

OPERATIONS: dict[str, Instruction] = {
    "push": Instruction(CallStack.push, stack_access=True, parameter_type=type.to_number),
    "pop": Instruction(CallStack.pop, stack_access=True),
    "duplicate": Instruction(CallStack.duplicate, stack_access=True),
    "copy": Instruction(CallStack.copy, stack_access=True, parameter_type=type.to_number),
    "slide": Instruction(CallStack.slide, stack_access=True, parameter_type=type.to_number),
    "swap": Instruction(CallStack.swap, stack_access=True),
    "add": Instruction(add, 2, store_return=True),
    "sub": Instruction(sub, 2, store_return=True),
    "mul": Instruction(mul, 2, store_return=True),
    "floordiv": Instruction(floordiv, 2, store_return=True),
    "mod": Instruction(mod, 2, store_return=True),
    "output number": Instruction(CallStack.pop_one, stack_access=True),
    "output character": Instruction(CallStack.pop_one, stack_access=True, return_type=type.to_character),
    "exit": Instruction(exit)
}