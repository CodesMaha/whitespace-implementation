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
    if call.parameter_amt: # items to pop from stack
        params.extend(stack.pop_many(call.parameter_amt))
    if call.parameter_type: # accept parameter from input
        params.append(call.parameter_type(matched_tokens[2]))
    
    if params:
        res = call.operator(*params)
    else: # no parameteres to pass in
        res = call.operator()

    if call.return_type:
        res = call.return_type(res) # convert here
    if call.store_return: # store in stack
        stack.push(res)
    
    return res