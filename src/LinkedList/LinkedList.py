class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
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