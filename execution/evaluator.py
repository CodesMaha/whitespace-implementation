""" map tokens from tokenization or lexical analysis to stack calls """

from execution.parser import OPERATIONS, Instruction
from execution.stack import CallStack

from typing import Any

class Evaluator:
    """ caller of funcs tokens respond to """
    def __init__(self, stack: CallStack):
        self.stack = stack # stack instance
        self.tokens = []
        self.imp_sep: str = "\n"

    @property
    def tokens(self) -> list[str]:
        """ get from tokenizer; shallow set """
        return self._matched_tokens
    @tokens.setter
    def tokens(self, new_matches) -> None:
        self._matched_tokens: list[str] = new_matches
        self.token_no: int = len(self._matched_tokens)
        self.pos: int = 0
        self.res: list[str] = []

    def _get_token(self, pos_incr: int = 0) -> str:
        return self._matched_tokens[self.pos + pos_incr]

    def _incr(self, incr: int = 1) -> None:
        self.pos += incr

    def evaluate(self) -> str:
        """ call funcs depending on curr tokens and Instruction """
        if self.pos == self.token_no:
            return self.imp_sep.join(self.res)

        params: list[Any] = []
        call: Instruction = OPERATIONS[self._get_token()]
        self._incr()

        if call.stack_access:
            params.append(self.stack)
        if call.parameter_amt: # items to pop from stack
            params.extend(self.stack.pop_many(call.parameter_amt))
        if call.parameter_type: # accept parameter from tokens
            params.append(
                call.parameter_type(self._get_token())
            ); self._incr()

        if params: # call and pass in params
            res: Any = call.operator(*params)
        else:
            res: Any = call.operator()

        if call.return_type: # convert return
            res = call.return_type(res)
        if call.store_return:
            self.stack.push(res)

        if not isinstance(res, str): # for join
            self.res.append(repr(res))
        else:
            self.res.append(res)

        return self.evaluate()
