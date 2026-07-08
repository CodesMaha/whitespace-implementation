""" map tokens to functions """

import execution.magic_functions as f

from dataclasses import dataclass
from collections.abc import Callable, Iterable
from typing import Any

@dataclass
class Instruction:
    operator: Callable 
    operand_amt: int = 0 # how many stack items to pop, or
    stack_access: bool = False # if access to stack (one more param)
    operand_type: Any = None

def sort_tokens(tokens: Iterable) -> list:
    """ sort appropriately since re goes with shortest """
    return sorted(tokens, key=len, reverse=True)

OPERATIONS: dict[str, Instruction] = {
    "push": Instruction(f.CallStack.push, 1, True, f.Number),
    "duplicate": Instruction(f.CallStack.duplicate, 0, True),
    "pop": Instruction(f.CallStack.pop, 0, True),
    "add": Instruction(f.add, 2),
    "sub": Instruction(f.sub, 2),
    "mul": Instruction(f.mul, 2),
    "floordiv": Instruction(f.floordiv, 2),
    "mod": Instruction(f.mod, 2)
}