""" map tokens from tokenization or lexical analysis to stack calls """

from execution.parser import OPERATIONS, Instruction
from execution import CallStack, Heap
from custom_operator import InputReader

from typing import Any

class Evaluator:
    """ caller of funcs tokens respond to """
    def __init__(
            self, heap: Heap | None = None,
            stack: CallStack | None = None, 
            *, verbose: bool = False
        ):
        # instances
        self.heap = heap or Heap()
        self.stack = stack or CallStack()
        self.input_reader = InputReader(self.heap)

        self.tokens = []
        self.verbose = verbose
        self.res_sep: str = "\n" if verbose else ""

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
        while self.pos < self.token_no:
            imp = self._get_token()
            if imp == "exit":
                break

            params: list[Any] = []
            call: Instruction = OPERATIONS[imp]
            self._incr()

            if call.input_access:
                params.append(self.input_reader)
            if call.heap_accesss:
                params.append(self.heap)
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

            if ( # check for verbosity exemptions
                (res is None) # no output produced
                or (not imp.startswith("output") and not self.verbose)
            ):
                continue
            
            if not isinstance(res, str): # for join
                self.res.append(repr(res))
            else:
                self.res.append(res)

        return self.res_sep.join(self.res)
