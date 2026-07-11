""" stack (linked list) of functions that are to be called """

from typing import Any
from errors.stack import EmptyStackError, MissingStackError, PopZeroError

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
    
    def peek_node(self, n=0) -> Node:
        """ internal and zero-indexed. retrieve specific Node """
        current_node: Node | None = self.head

        if current_node is None:
            raise EmptyStackError("No top calls or calls after to peek.")
        
        for _ in range(n): # will not run if zero
            if current_node.next is None:
                raise MissingStackError(f"Cannot access stack item {n}.")
            current_node = current_node.next
        return current_node
    
    def peek(self) -> Any:
        """ external and only for top call """
        return self.peek_node(0).value
    
    def peek_all(self) -> list:
        """ 
        internal. can be used for testing and printing all current calls
        Node.value -> Node.value where None is excluded
        """
        current_node: None | Node = self.head
        
        peeked_vals: list = [] # to append to
        while current_node is not None:
            peeked_vals.append(current_node.value)
            current_node = current_node.next

        return peeked_vals # empty list if top is None
    
    def push_many(self, values: list[int]) -> None:
        """ internal. also can be for testing. just call .push in loop """
        for value in values:
            self.push(value)
    
    def push(self, value: int) -> str:
        """ push to stack then return pushed. accepts from Number """
        node = Node(value)
        if self.head: # not None
            node.next = self.head
        self.head = node
        self.size += 1 # increase stack count
        return f"pushed {self.head.value}" # info msg
    
    def pop_many(self, n: int) -> list[Any]:
        """ 
        internal and one-indexed. 
        retrieving list of Node.value until stack item n.
        can be used for function parameters 
        """
        if (n <= 0) or (self.is_empty()):
            raise PopZeroError
        
        popped_vals: list[Any] = [] # to append to
        while len(popped_vals) < n:
            if self.head is None:
                raise PopZeroError(f"Cannot access stack item {n}. Current stack size: {self.size}.")
            popped_vals.append(self.head.value) # top call
            self.head = self.head.next # next call
            self.size -= 1

        return popped_vals
    
    def pop(self) -> str:
        """ 
        pop top of stack then return popped.
        arg amount should be above zero.
        arg internal False if externally called
        """
        popped_node = self.pop_many(1)[0]
        return f"popped {popped_node}" # info msg
    
    def duplicate(self) -> str:
        """ duplicate top of stack """
        if self.is_empty():
            raise EmptyStackError(f"No top call to duplicate. Current stack size: {self.size}.")
        self.push(self.head.value) # also handles self.size+=1
        return f"duplicated {self.head.value}" # info msg
    
    def copy(self, n: int) -> str:
        """ copy nth item to top of stack, where n is zero-indexed """
        to_copy: Node = self.peek_node(n)
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
            raise MissingStackError(f"Cannot slide off top item or before. Current stack size: {self.size}.")
        elif n == self.size-2:
            self.head.next = None
            self.size = 1
            return "slid off all"
        
        # if self.peek is zero-indexed then zero is top, so +1
        slide_end: Node = self.peek_node(n+1) # after n items
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