""" stack (linked list) of functions that are to be called """

from typing import Any
from errors.stack import EmptyStackError, MissingStackError

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
        """ retrieve specific Node. zero-indexed """
        current_head: Node | None = self.head

        if current_head is None:
            raise EmptyStackError("No top calls or calls after to peek.")
        
        for _ in range(n): # will not run if zero
            if current_head.next is None:
                raise MissingStackError(f"Cannot access stack item {n}.")
            current_head = current_head.next
        return current_head
    
    def peek_many(self, n: int) -> list[Any]:
        """ 
        internal and one-indexed. 
        retrieving list of Node.value until stack item n.
        can be used for function parameters 
        """
        peeked_nodes: list[Any] = [] # to append to
        
        current_node = self.head
        for _ in range(n): # will not run at zero
            if current_node is None:
                raise MissingStackError(f"Cannot access stack item {n}. Current stack size: {self.size}")
            peeked_nodes.append(current_node.value)
            current_node = current_node.next

        return peeked_nodes
    
    def push(self, value: int) -> str:
        """ push to stack then return pushed. accepts from Number """
        node = Node(value)
        if self.head: # not None
            node.next = self.head
        self.head = node
        self.size += 1 # increase stack count
        return f"pushed {self.head.value}" # info msg
    
    def pop(self) -> str:
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
        """ 
        keep only top of stack. 
        discard n.value then keep n.next.
        zero-indexed and not lazily evaluated
        """
        if self.is_empty():
            raise EmptyStackError(f"Cannot slide {n} items after top of stack if top does not exist.")
        elif self.size == 1:
            return "no items to slide off"
        
        # self.size counts from idx 1 and includes top, so -2
        if n > self.size-2:
            raise MissingStackError(f"Cannot slide off top item or before. Current stack size: {self.size}")
        elif n == self.size-2:
            self.head.next = None
            self.size = 1
            return "slid off all"
        
        # if self.peek is zero-indexed then zero is top, so +1
        slide_end = self.peek(n+1) # after n items
        self.head.next = slide_end.next # keep n.next
        self.size -= n + 1
        return f"slid {n} items"

    def swap(self) -> str:
        """ swap top item of stack with next item """
        if self.size < 2:
            raise MissingStackError("Cannot swap top two stack items if none exist.")
        
        first_node: Node = self.head # top node
        second_node: Node = self.head.next # second node

        first_node.next = second_node.next # third node
        second_node.next = first_node

        self.head = second_node # top now second call

        return f"swapped from {first_node.value} to {second_node.value}"