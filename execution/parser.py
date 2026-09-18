""" map tokens to functions """

# parameter types
import custom_operator as c_op

# operations
from execution import Stack, Heap
from operator import add, sub, mul, mod

from dataclasses import dataclass
from collections.abc import Callable

@dataclass
class Instruction:
    operator: Callable | None = None
    parameter_amt: int = 0 # how many stack items to pop
    parameter_type: Callable | None = None
    return_type: Callable | None = None
    store_return: bool = False # push to stack
    input_access: bool = False # requires input instance
    stack_access: bool = False # requires stack instance
    heap_accesss: bool = False # requires heap instance

OPERATIONS: dict[str, Instruction] = {
    "push": Instruction(Stack.push, stack_access=True, parameter_type=c_op.to_number),
    "pop": Instruction(Stack.pop, stack_access=True),
    "duplicate": Instruction(Stack.duplicate, stack_access=True),
    "copy": Instruction(Stack.copy, stack_access=True, parameter_type=c_op.to_number),
    "slide": Instruction(Stack.slide, stack_access=True, parameter_type=c_op.to_number),
    "swap": Instruction(Stack.swap, stack_access=True),
    "add": Instruction(add, 2, store_return=True),
    "sub": Instruction(sub, 2, store_return=True),
    "mul": Instruction(mul, 2, store_return=True),
    "div": Instruction(c_op.integer_div, 2, store_return=True),
    "mod": Instruction(mod, 2, store_return=True),
    "store": Instruction(Heap.store, 2, heap_accesss=True),
    "retrieve": Instruction(Heap.retrieve, 1, store_return=True, heap_accesss=True),
    "input character": Instruction(c_op.InputReader.read_character, 1, input_access=True),
    "input number": Instruction(c_op.InputReader.read_number, 1, input_access=True),
    "output character": Instruction(Stack.pop_one, stack_access=True, return_type=c_op.to_character),
    "output number": Instruction(Stack.pop_one, stack_access=True),
    "exit": Instruction()
}
