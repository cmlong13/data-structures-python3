class Queue:
    """
    a simple implementation of a queue data structure using a list. The queue follows the First-In-First-Out (FIFO) principle, where elements are added to the end of the queue and removed from the front. The class provides methods for enqueueing, dequeueing, checking if the queue is empty, and getting the size of the queue.
     - enqueue(item): Add an item to the end of the queue.
     - dequeue(): Remove and return the item from the front of the queue.
     - is_empty(): Check if the queue is empty.
     - size(): Get the number of items in the queue.
     - clear(): Remove all items from the queue.
     - peek(): Return the item at the front of the queue without removing it.
    
    """
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    def size(self):
        return len(self.queue)
    
    def __str__(self):
        return str(self.queue)
    
    def clear(self):
        self.queue = []

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("can not peek from empty queue")
    
