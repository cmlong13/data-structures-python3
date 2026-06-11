# Queue

A **queue** is a linear data structure that follows the **FIFO** principle:

> **First In, First Out**

This means the first item added is the first item removed.

---

## Implementation

This queue is implemented in Python using a list as the internal storage.

File location:

```text
src/queue/queue.py
```

---

## Operations

| Operation | Description | Time Complexity |
|----------|-------------|-----------------|
| `enqueue(value)` | Adds an item to the back | O(1) |
| `dequeue()` | Removes and returns the front item | O(n) |
| `peek()` | Returns the front item without removing it | O(1) |
| `is_empty()` | Checks if the queue is empty | O(1) |
| `size()` | Returns the number of items | O(1) |
| `clear()` | Removes all items | O(n) |

---

## Example

```python
from src.queue.queue import queue

queue = queue()

queue.enqueue(10)
queue.enqueue(20)

print(queue.peek())     # 10
print(queue.dequeue())  # 10
print(queue.size())     # 1
```

---

## Common Uses

Queues are used in:

- Task scheduling
- Print queues
- Breadth-first search
- Message queues
- Request handling

---

## Testing

Tests are located in:

```text
tests/tests-queue.py
```

Run tests with:

```bash
python tests/tests-queue.py
```
