""" map tokens from tokenization or lexical analysis to stack calls """

from execution.parser import OPERATIONS, Instruction
from execution import Stack, Heap
from custom_operator import InputReader, Subroutines

from collections.abc import Iterator
from typing import Any

class Evaluator:
    """ caller of funcs tokens respond to """
    def __init__(
            self, heap: Heap | None = None,
            stack: Stack | None = None, 
            *, verbose: bool = False
        ):
        # instances
        self.heap = heap or Heap()
        self.stack = stack or Stack()
        self.input_reader = InputReader(self.heap)
        self.subroutines = Subroutines()

        self.tokens = []
        self.verbose = verbose

    @property
    def tokens(self) -> list[str]:
        """ get from tokenizer; shallow set """
        return self._matched_tokens
    @tokens.setter
    def tokens(self, new_matches) -> None:
        self._matched_tokens: list[str] = new_matches
        self.token_no: int = len(self._matched_tokens)
        self.pos: int = 0 # current token <= total token_no
        self.subroutines.read_tokens(new_matches)

    def _get_token(self, pos_incr: int = 0) -> str:
        return self._matched_tokens[self.pos + pos_incr]

    def _incr(self, incr: int = 1) -> None:
        self.pos += incr

    def on_subroutine_call(self, label: str) -> None:
        """ extend next tokens to match those of subroutine """
        new_tokens = self.subroutines.get_subroutine(label)
        self._matched_tokens[self.pos:self.pos] = new_tokens
        self.token_no += len(new_tokens)

    def on_flow_operation(self, op: str) -> None:
        if (op == "jump if zero") and (self.stack.pop_one() != 0):
            self._incr()
            return
        elif (op == "jump if negative") and (self.stack.pop_one() >= 0):
            self._incr()
            return
        label = self._get_token(); self._incr()
        self.on_subroutine_call(label)

    def format_verbose(
        self, verbose_out: str, 
        is_first_instruction: bool,
        has_single_param_instruction: bool
    ) -> str:
        """ decide cases for newlines """
        if self.token_no == 1: 
            return verbose_out # single instruction
        elif has_single_param_instruction:
            return verbose_out # single instruction with param
        elif is_first_instruction:
            return f"{verbose_out}\n" # no start newline
        elif self.pos == self.token_no:
            return f"\n{verbose_out}" # no end newline
        
        return f"\n{verbose_out}\n"
        

    def evaluate(self) -> Iterator[str]:
        """ call funcs depending on curr tokens and Instruction """

        while self.pos < self.token_no:
            is_first_instruction = self.pos == 0

            imp = self._get_token()
            if imp == "exit":
                break

            params: list[Any] = []
            call: Instruction = OPERATIONS[imp]

            if call.input_access:
                params.append(self.input_reader)
            if call.heap_accesss:
                params.append(self.heap)
            if call.stack_access:
                params.append(self.stack)
            if call.subroutines_access:
                params.append(self.subroutines)

            self._incr() # skip imp
            
            if call.parameter_amt: # items to pop from stack
                params.extend(self.stack.pop_many(call.parameter_amt))
            if call.parameter_type: # accept parameter from tokens
                params.append(
                    call.parameter_type(self._get_token())
                ); self._incr() # skip param

            if imp == "call subroutine":
                params.append(self.pos)
            if call.subroutines_access:
                res = call.operator(*params)
                if res is not None: self.pos = res
                continue

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
            
            res = res if isinstance(res, str) else repr(res)

            # verbose instructions should be in a sea of newlines
            if (not imp.startswith("output") and self.verbose):
                res = self.format_verbose(
                    res, is_first_instruction, 
                    (self.token_no == 2) and (call.parameter_type)
                )

            yield res

    def consumed_eval(self) -> str:
        """ mainly for the purpose of testing """
        return "".join(self.evaluate())
