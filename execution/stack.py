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
    
    def peek(self, n=0) -> Node:
        """ retrieve specific Node. zero-indexed, where n=0 is top Node """
        current_head = self.head
        for _ in range(n): # will not run if zero
            if current_head.next == None:
                raise EmptyStackError(f"Cannot access stack item {n}.")
            current_head = current_head.next
        return current_head
    
    def peek_many(self, n: int) -> list[Any]:
        """ internal. retrieving list of Node.value until stack item n """
        peeked_nodes: list[Any] = [] # to append to

        current_node: Node = self.head
        for _ in range(n): # will not run at zero
            if current_node == None:
                raise EmptyStackError(f"Cannot access stack item {n}. Current stack size: {self.size}")
            peeked_nodes.append(current_node.value)
            current_node = current_node.next

        return peeked_nodes
    
    def push(self, value: int) -> str:
        """ push to stack then return pushed """
        node = Node(value)
        if self.head: # not None
            node.next = self.head
        self.head = node
        self.size += 1 # increase stack count
        return f"pushed {self.head.value}" # info msg
    
    def pop(self) -> list[Any] | str:
        """ 
        pop top of stack then return popped.
        arg amount should be above zero.
        arg internal False if externally called
        """
        if self.is_empty():
            raise EmptyStackError(f"Cannot pop top item. Current stack size: {self.size}.")
        
        popped_node = self.head.value # top call
        self.head = self.head.next # next call
        self.size -= 1

        return f"popped {popped_node}" # info msg
    
    def duplicate(self) -> str:
        """ duplicate top of stack """
        if self.is_empty():
            raise EmptyStackError(f"No top call to duplicate. Current stack size: {self.size}.")
        self.push(self.head.value) # also handles self.size+=1
        return f"duplicated {self.head.value}" # info msg
    
    def copy(self, n: int) -> str:
        """ copy nth item to top of stack, where n is zero-indexed """
        to_copy = self.peek(n)
        self.push(to_copy.value)
        return f"copied {to_copy.value}" # info msg
    
    def slide(self, n: int) -> str:
        """ keep only top of stack. discard n after, where n > 0 """
        if self.is_empty():
            raise EmptyStackError(f"Cannot slide {n} items after top of stack if top does not exist.")
        elif self.size == 1:
            return "no items to slide off"
        elif n == 0: # TODO: does this error?
            return "cannot slide zero items"
        
        slide_end = self.peek(n+1) # after n items
        self.head.next = slide_end
        self.size -= n
        return f"slided {n} items until {slide_end.value}"

    def swap(self) -> str:
        """ swap top item of stack with next item """
        first_node: Node = self.head
        second_node: Node = self.head.next

        self.head = second_node
        self.head.next = first_node

        return f"swapped from {first_node.value} to {second_node.value}"