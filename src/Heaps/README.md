# Min Heap

A **min heap** is a tree-based data structure where the smallest value is always kept at the root.

For every parent node:

- The parent value is less than or equal to its child values
- The minimum value can be accessed quickly from the root

This makes min heaps useful when you need repeated access to the smallest item.

---

## Implementation

This min heap is implemented in Python using a list as the internal storage.

File location:

```text
src/Heaps/MinHeap.py
```

The heap uses array indexes to represent parent and child relationships:

- Left child: `2 * index + 1`
- Right child: `2 * index + 2`
- Parent: `(index - 1) // 2`

---

## Operations

| Operation | Description | Time Complexity |
|----------|-------------|-----------------|
| `insert(key)` | Adds a value and restores the heap property | O(log n) |
| `peek()` | Returns the smallest value without removing it | O(1) |
| `remove_min()` | Removes and returns the smallest value | O(log n) |
| `is_empty()` | Checks if the heap has no values | O(1) |
| `len(heap)` | Returns the number of values in the heap | O(1) |

---

## Example

```python
from src.Heaps.MinHeap import MinHeap

heap = MinHeap()

heap.insert(30)
heap.insert(10)
heap.insert(20)

print(heap.peek())        # 10
print(heap.remove_min())  # 10
print(len(heap))          # 2
```

---

## Common Uses

Min heaps are used in:

- Priority queues
- Dijkstra's shortest path algorithm
- Event scheduling
- Merging sorted data
- Finding the smallest items efficiently

---

## Testing

Tests are located in:

```text
tests/TestsMinHeap.py
```

Run tests with:

```bash
python tests/TestsMinHeap.py
```

Or run the full test suite with:

```bash
pytest
```
