class Stack:

    """
    A simple implementation of a stack data structure in Python.
    The stack supports the following operations:
    - push(item): Add an item to the top of the stack.
    - pop(): Remove and return the item from the top of the stack.
    - peek(): Return the item from the top of the stack without removing it.
    - is_empty(): Check if the stack is empty.
    - size(): Return the number of items in the stack.
    - clear(): Remove all items from the stack.
    """

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("can not peek from empty stack")
        
    def size(self):
        return len(self.stack)
    
    def clear(self):
        self.stack = []
    
    def __str__(self):
        return str(self.stack)