""" stack (linked list) of functions that are to be called """

from typing import Any
from errors.stack import EmptyStackError, ZeroPopError
from execution.magic_functions import Number

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
    
    def push(self, value: Number) -> str:
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
    
    def duplicate(self) -> str:
        """ duplicate top of stack """
        if self.is_empty():
            raise EmptyStackError(f"No top call to duplicate. Current stack size: {self.size}.")
        self.push(self.head.value)
        return f"duplicated {self.head.value}" # info msg
    
    def copy(self, n: Number) -> str:
        """ copy nth item to top of stack, where n=0 is top (zero-indexed) """
        current_head = self.head # top of stack, or item zero
        for _ in range(n):
            if self.head.next == None:
                raise EmptyStackError(f"No stack item {n} to copy to top.")
            current_head = self.head.next
        self.push(current_head.value)
        return f"copied {current_head.value}"
    
    def slide(self) -> str:
        """ keep only top of stack """
        self.head.next = None
        self.size = 1
        return f"slided all except {self.head.value} off"

    def swap(self) -> str:
        """ swap top item of stack with next item """
        first_node: Node = self.head
        second_node: Node = self.head.next

        self.head = second_node
        self.head.next = first_node

        return f"swapped from {first_node.value} to {second_node.value}"