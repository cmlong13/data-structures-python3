# Linked List

A **linked list** is a linear data structure made of nodes, where each node stores a value and a reference to the next node.

This implementation is a **singly linked list**, which means each node points only to the next node in the list.

---

## Implementation

This linked list is implemented in Python using a `Node` class and a `LinkedList` class.

File location:

```text
src/LinkedList/LinkedList.py
```

---

## Operations

| Operation | Description | Time Complexity |
|----------|-------------|-----------------|
| `append(value)` | Adds an item to the end | O(n) |
| `prepend(value)` | Adds an item to the beginning | O(1) |
| `insert(index, value)` | Adds an item at a specific index | O(n) |
| `get(index)` | Returns the item at a specific index | O(n) |
| `find(value)` | Returns the index of the first matching item | O(n) |
| `set(index, value)` | Updates the item at a specific index | O(n) |
| `remove_at(index)` | Removes the item at a specific index | O(n) |
| `remove(value)` | Removes the first matching item | O(n) |
| `is_empty()` | Checks if the linked list is empty | O(1) |
| `size()` | Returns the number of items | O(1) |
| `clear()` | Removes all items | O(1) |
| `to_list()` | Returns the linked list values as a Python list | O(n) |

---

## Example

```python
from src.LinkedList.LinkedList import LinkedList

linked_list = LinkedList()

linked_list.append(10)
linked_list.append(30)
linked_list.insert(1, 20)

print(linked_list.get(1))   # 20
print(linked_list.find(30)) # 2
print(linked_list.size())   # 3
```

---

## Common Uses

Linked lists are used in:

- Dynamic memory allocation
- Implementing stacks and queues
- Undo and redo systems
- Hash table chaining
- Graph adjacency lists

---

## Testing

Tests are located in:

```text
tests/TestsLinkedList.py
```

Run tests with:

```bash
python tests/TestsLinkedList.py
```
