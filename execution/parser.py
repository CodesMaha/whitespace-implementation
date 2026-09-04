""" map tokens to functions """

# parameter types
import lexer.to_type as type

# operations
from execution import CallStack, Heap
from operator import add, sub, mul, mod
from sys import exit

from dataclasses import dataclass
from collections.abc import Callable

@dataclass
class Instruction:
    operator: Callable | None = None
    parameter_amt: int = 0 # how many stack items to pop
    parameter_type: Callable | None = None
    return_type: Callable | None = None
    store_return: bool = False # push to stack
    stack_access: bool = False # requires stack instance
    heap_accesss: bool = False # requires heap instance

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
    "div": Instruction(type.integer_div, 2, store_return=True),
    "mod": Instruction(mod, 2, store_return=True),
    "store": Instruction(Heap.store, 2, heap_accesss=True),
    "retrieve": Instruction(Heap.retrieve, 1, store_return=True, heap_accesss=True),
    "output number": Instruction(CallStack.pop_one, stack_access=True),
    "output character": Instruction(CallStack.pop_one, stack_access=True, return_type=type.to_character),
    "exit": Instruction()
}
