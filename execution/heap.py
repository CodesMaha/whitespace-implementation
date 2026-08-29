""" heap? storage and retrieval with memory addresses """

from typing import Any
from errors.memory import AddressNotFoundError

class Heap:
    def __init__(self):
        self._heap: dict[Any, Any] = {}

    @property
    def heap_dict(self):
        """ like CallStack.peek_all; 
        internal and can be used for testing 
        """
        return self._heap

    def store(self, second_stack: Any, top_stack: Any) -> None:
        """ arg top_stack value; arg second_stack addr """
        self._heap.update({second_stack: top_stack})

    def retrieve(self, top_stack: Any) -> Any:
        """ from key as top_stack addr """
        try:
            return self._heap[top_stack]
        except KeyError as exc:
            raise AddressNotFoundError(address=top_stack) from exc
