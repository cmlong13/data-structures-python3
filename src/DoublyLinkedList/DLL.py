class Node:
    """
    A node in a doubly linked list.
    
    Attributes:
    - value: The value stored in the node.
    - next: A reference to the next node in the list.  
    - prev: A reference to the previous node in the list.

    """
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """
    A doubly linked list implementation in Python.

    Methods:
    - is_empty(): Returns True if the list is empty, False otherwise.
    - size(): Returns the number of nodes in the list.
    - append(value): Adds a new node with the given value to the end of the list.
    - prepend(value): Adds a new node with the given value to the beginning of the list.
    - insert(index, value): Inserts a new node with the given value at the specified index.
    - get(index): Returns the value of the node at the specified index.
    - find(value): Returns the index of the first node with the given value, or raises ValueError if not found.
    - set(index, value): Updates the value of the node at the specified index.
    - remove_at(index): Removes the node at the specified index.
    - remove(value): Removes the first node with the given value.
    - clear(): Removes all nodes from the list.
    - __str__(): Returns a string representation of the list.
    - to_list(): Returns a Python list containing all the values in the linked list. 

    """
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        def prepend(self, value):
            new_node = Node(value)
            if self.is_empty():
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node

            def to_list(self):
                result = []
                current = self.head
                while current:
                    result.append(current.value)
                    current = current.next
                return result
            
            def reverse_list(self):
                result = []
                current = self.tail
                while current:
                    result.append(current.value)
                    current = current.prev
                return result
            
            def get(self, index):
                if index < 0 or index >= self.size():
                    raise IndexError("Index out of bounds")
                
                current = self.head
                for _ in range(index):
                    current = current.next
                return current.value
            
            def find(self, value):
                current = self.head
                index = 0
                while current:
                    if current.value == value:
                        return index
                    current = current.next
                    index += 1
                raise ValueError("Value not found in list")
            
            def set(self, index, value):
                if index < 0 or index >= self.size():
                    raise IndexError("Index out of bounds")
                
                current = self.head
                for _ in range(index):
                    current = current.next
                current.value = value

            def insert(self, index, value):
                if index < 0 or index > self.size():
                    raise IndexError("Index out of bounds")
                
                new_node = Node(value)
                
                if index == 0:
                    new_node.next = self.head
                    if self.head:
                        self.head.prev = new_node
                    self.head = new_node
                    if self.tail is None:
                        self.tail = new_node
                elif index == self.size():
                    self.tail.next = new_node
                    new_node.prev = self.tail
                    self.tail = new_node
                else:
                    current = self.head
                    for _ in range(index - 1):
                        current = current.next
                    new_node.next = current.next
                    new_node.prev = current
                    current.next.prev = new_node
                    current.next = new_node

            def remove_at(self, index):
                if index < 0 or index >= self.size():
                    raise IndexError("Index out of bounds")
                
                if index == 0:
                    if self.head.next:
                        self.head = self.head.next
                        self.head.prev = None
                    else:
                        self.head = None
                        self.tail = None
                elif index == self.size() - 1:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    current = self.head
                    for _ in range(index):
                        current = current.next
                    current.prev.next = current.next
                    current.next.prev = current.prev

            def remove(self, value):
                current = self.head
                while current:
                    if current.value == value:
                        if current.prev:
                            current.prev.next = current.next
                        else:
                            self.head = current.next
                        if current.next:
                            current.next.prev = current.prev
                        else:
                            self.tail = current.prev
                        return
                    current = current.next
                raise ValueError("Value not found in list")
            
            def clear(self):
                self.head = None
                self.tail = None

            def __str__(self):
                values = []
                current = self.head
                while current:
                    values.append(str(current.value))
                    current = current.next
                return " <-> ".join(values)