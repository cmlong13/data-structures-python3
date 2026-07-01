# Doubly Linked List

A **doubly linked list** is a linear data structure made of nodes, where each node stores a value, a reference to the next node, and a reference to the previous node.

This makes it possible to traverse the list forward from the head or backward from the tail.

---

## Implementation

This doubly linked list is implemented in Python using a `Node` class and a `DoublyLinkedList` class.

File location:

```text
src/DoublyLinkedList/DLL.py
```

---

## Operations

| Operation | Description | Time Complexity |
|----------|-------------|-----------------|
| `append(value)` | Adds an item to the end | O(1) |
| `prepend(value)` | Adds an item to the beginning | O(1) |
| `insert(index, value)` | Adds an item at a specific index | O(n) |
| `get(index)` | Returns the item at a specific index | O(n) |
| `find(value)` | Returns the index of the first matching item | O(n) |
| `set(index, value)` | Updates the item at a specific index | O(n) |
| `remove_at(index)` | Removes the item at a specific index | O(n) |
| `remove(value)` | Removes the first matching item | O(n) |
| `is_empty()` | Checks if the doubly linked list is empty | O(1) |
| `size()` | Returns the number of items | O(1) |
| `clear()` | Removes all items | O(1) |
| `to_list()` | Returns the values from head to tail as a Python list | O(n) |
| `reverse_list()` | Returns the values from tail to head as a Python list | O(n) |

---

## Example

```python
from src.DoublyLinkedList.DLL import DoublyLinkedList

dll = DoublyLinkedList()

dll.append(10)
dll.append(30)
dll.insert(1, 20)

print(dll.get(1))        # 20
print(dll.to_list())     # [10, 20, 30]
print(dll.reverse_list()) # [30, 20, 10]
```

---

## Common Uses

Doubly linked lists are used in:

- Browser history
- Undo and redo systems
- LRU caches
- Music playlists
- Deques

---

## Testing

Tests are located in:

```text
tests/TestsDoublyLinkedList.py
```

Run tests with:

```bash
python tests/TestsDoublyLinkedList.py
```
