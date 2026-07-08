""" map tokens from tokenization or lexical analysis to stack calls """

from lexer.tokens import TOKENS
from execution.parser import OPERATIONS, Instruction
from execution.stack import CallStack

from collections.abc import Iterable, Callable
from typing import Any

def evaluate_tokens(matched_tokens: Iterable, stack: CallStack) -> Callable | Any:
    """ arg matched_tokens must have at least two items """
    call: Instruction = OPERATIONS[TOKENS[matched_tokens[0]][matched_tokens[1]]]
    params = [] # to append to and extend

    if call.stack_access:
        params.append(stack) # current stack instance
    if call.operand_type:
        params.append(call.operand_type(matched_tokens[2]).value)
    elif call.operand_amt: # items to pop from stack
        params.extend(stack.peek_many(call.operand_amt))
    
    if params:
        return call.operator(*params)
    else:
        return call.operator()