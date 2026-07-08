""" stack (linked list) of functions that are to be called """

from typing import Any
from errors.stack import EmptyStackError, ZeroPopError

class Node:
    """ single node for function call """
    def __init__(self, value: Any):
        self.value: Any = value # top
        self.next: Node | None = None # next call

class CallStack:
    """ linked list for function calls """
    def __init__(self):
        self.head: Node | None = None
        self.size = 0

    def is_empty(self) -> bool:
        """ check if stack is empty """
        return self.size == 0
    
    def duplicate(self) -> str:
        """ duplicate top of stack """
        if self.is_empty():
            raise EmptyStackError(f"No top call to duplicate. Current stack size: {self.size}.")
        self.push(self.head.value)
        return f"duplicated {self.head.value}" # info msg
    
    def push(self, value: Any) -> str:
        """ push to stack then return pushed """
        node = Node(value)
        if self.head: # not None
            node.next = self.head
        self.head = node
        self.size += 1 # increase stack count
        return f"pushed {self.head.value}" # info msg
    
    def pop(self, amount=1, internal=False) -> list[Any] | str:
        """ 
        pop top of stack then return popped.
        arg amount should be above zero.
        arg internal False if externally called
        """
        popped_nodes: list[Any] = [] # to append to

        if amount <= 0:
            raise ZeroPopError

        while len(popped_nodes) < amount:
            if self.is_empty():
                raise EmptyStackError(f"Cannot pop {amount} time(s). Current stack size: {self.size}.")
            popped_nodes.append(self.head.value) # top call
            self.head = self.head.next # next call
            self.size -= 1

        if (len(popped_nodes) == 1) and (not internal):
            return f"popped {popped_nodes[0]}" # info msg
        return popped_nodes