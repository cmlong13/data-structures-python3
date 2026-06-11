class Node:
    """
    A node in a singly linked list.

    """
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """
    A singly linked list.

    Attributes:        
        head: The first node in the list.
        size: The number of nodes in the list
    
    Methods:
        is_empty(): Returns True if the list is empty, False otherwise.
        size(): Returns the number of nodes in the list.
        append(value): Adds a new node with the given value to the end of the list.
        prepend(value): Adds a new node with the given value to the beginning of the list.
        insert(index, value): Inserts a new node with the given value at the specified index.
        get(index): Returns the value of the node at the specified index.
        find(value): Returns the index of the first node with the given value, or raises ValueError if not found.
        set(index, value): Updates the value of the node at the specified index.
        remove_at(index): Removes the node at the specified index.
        remove(value): Removes the first node with the given value.
        clear(): Removes all nodes from the list.
        __str__(): Returns a string representation of the list.
        to_list(): Returns a Python list containing all the values in the linked list.
    
    """
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size
    
    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        
        new_node = Node(value)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        
        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
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
        raise ValueError("Value not found in the list")
    
    def set(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        
        self.size -= 1

    def remove(self, value):
        current = self.head
        previous = None
        
        while current:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.size -= 1
                return
            previous = current
            current = current.next
        raise ValueError("Value not found in the list")
    
    def clear(self):
        self.head = None
        self.size = 0
    
    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values)
    
    def to_list(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values
    