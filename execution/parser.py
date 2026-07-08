""" map tokens to functions """

import execution.magic_functions as f
from execution.stack import CallStack

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
    "push": Instruction(CallStack.push, 0, f.Number, True),
    "pop": Instruction(CallStack.pop, stack_access=True),
    "duplicate": Instruction(CallStack.duplicate, stack_access=True),
    "copy": Instruction(CallStack.copy, 0, f.Number, True),
    "slide": Instruction(CallStack.slide, stack_access=True),
    "swap": Instruction(CallStack.swap, stack_access=True),
    "add": Instruction(f.add, 2),
    "sub": Instruction(f.sub, 2),
    "mul": Instruction(f.mul, 2),
    "floordiv": Instruction(f.floordiv, 2),
    "mod": Instruction(f.mod, 2),
    "exit": Instruction(f.exit)
}