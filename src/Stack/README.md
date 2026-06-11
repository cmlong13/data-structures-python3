# Stack

A **stack** is a linear data structure that follows the **LIFO** principle:

> **Last In, First Out**

This means the last item added is the first item removed.

---

## Implementation

This stack is implemented in Python using a list as the internal storage.

File location:

```text
src/Stack/Stack.py
```

---

## Operations

| Operation | Description | Time Complexity |
|----------|-------------|-----------------|
| `push(value)` | Adds an item to the top | O(1) |
| `pop()` | Removes and returns the top item | O(1) |
| `peek()` | Returns the top item without removing it | O(1) |
| `is_empty()` | Checks if the stack is empty | O(1) |
| `size()` | Returns the number of items | O(1) |
| `clear()` | Removes all items | O(n) |

---

## Example

```python
from src.Stack.Stack import Stack

stack = Stack()

stack.push(10)
stack.push(20)

print(stack.peek())  # 20
print(stack.pop())   # 20
print(stack.size())  # 1
```

---

## Common Uses

Stacks are used in:

- Undo and redo systems
- Browser history
- Function call stacks
- Backtracking
- Depth-first search

---

## Testing

Tests are located in:

```text
tests/TestsStack.py
```

Run tests with:

```bash
python tests/TestsStack.py
```
