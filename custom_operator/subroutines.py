""" storing labels and jumping to them """

from errors.memory import LabelNotFoundError

class Subroutines:
    """ storing token positions for the evaluator to jump to """
    def __init__(self):
        self.prev_context: list[None | int] = []
        self.read_tokens([])

    @staticmethod
    def _get_label_index(tokens: list[str], start_idx: int = 0) -> int | None:
        """ get index of next \"mark label\" token """
        try:
            label_pos: int | None = tokens.index("mark label", start_idx)
        except ValueError:
            label_pos = None
        
        return label_pos

    def read_tokens(self, tokens: list[str]) -> None:
        """ read tokens to store all label positions """
        self.labels: dict[str, int] = {}
        label_pos = Subroutines._get_label_index(tokens)
        while label_pos is not None:
            self.labels[tokens[label_pos + 1]] = label_pos
            label_pos = Subroutines._get_label_index(tokens, label_pos + 1)

    def call_subroutine(self, label: str, curr_pos: int) -> int:
        """ store current position and return position to label """
        # curr token is "call subroutine", so use next
        self.prev_context.append(curr_pos + 1)
        return self.jump(label)

    def end_subroutine(self) -> int:
        """ try to get position of previous context """
        if not self.prev_context:
            return
        return self.prev_context.pop()

    def jump(self, label: str) -> int:
        """ look up position of label """
        try:
            return self.labels[label]
        except KeyError as exc:
            raise LabelNotFoundError(label=label) from exc

    def jump_if_zero(self, stack_val: int, label: str) -> int | None:
        """ call self.jump if stack_val == 0 """
        return self.jump(label) if stack_val == 0 else None

    def jump_if_negative(self, stack_val: int, label: str) -> int | None:
        """ call self.jump if stack_val is less than 0 """
        return self.jump(label) if stack_val < 0 else None
