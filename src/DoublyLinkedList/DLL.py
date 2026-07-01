class Node:
    """
    A node in a doubly linked list.

    Attributes:
        value: The value stored in the node.
        next: A reference to the next node in the list.
        prev: A reference to the previous node in the list.

    """
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    A doubly linked list implementation in Python.

    Methods:
        is_empty(): Returns True if the list is empty, False otherwise.
        size(): Returns the number of nodes in the list.
        append(value): Adds a new node with the given value to the end of the list.
        prepend(value): Adds a new node with the given value to the beginning of the list.
        insert(index, value): Inserts a new node with the given value at the specified index.
        get(index): Returns the value of the node at the specified index.
        find(value): Returns the index of the first node with the given value.
        set(index, value): Updates the value of the node at the specified index.
        remove_at(index): Removes the node at the specified index.
        remove(value): Removes the first node with the given value.
        clear(): Removes all nodes from the list.
        to_list(): Returns a Python list of values from head to tail.
        reverse_list(): Returns a Python list of values from tail to head.
        __str__(): Returns a string representation of the list.

    """
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def append(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self._size += 1

    def prepend(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self._size += 1

    def insert(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.prepend(value)
        elif index == self._size:
            self.append(value)
        else:
            next_node = self._node_at(index)
            previous_node = next_node.prev
            new_node = Node(value)

            new_node.prev = previous_node
            new_node.next = next_node
            previous_node.next = new_node
            next_node.prev = new_node
            self._size += 1

    def get(self, index):
        return self._node_at(index).value

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
        self._node_at(index).value = value

    def remove_at(self, index):
        node = self._node_at(index)

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        self._size -= 1

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

                self._size -= 1
                return

            current = current.next

        raise ValueError("Value not found in the list")

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0

    def to_list(self):
        values = []
        current = self.head

        while current:
            values.append(current.value)
            current = current.next

        return values

    def reverse_list(self):
        values = []
        current = self.tail

        while current:
            values.append(current.value)
            current = current.prev

        return values

    def __str__(self):
        return " <-> ".join(str(value) for value in self.to_list())

    def _node_at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")

        if index < self._size / 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self._size - 1, index, -1):
                current = current.prev

        return current
