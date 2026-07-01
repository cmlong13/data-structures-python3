# Binary Search Tree

A **binary search tree** is a node-based data structure where each node can have a left child and a right child.

For every node:

- Values smaller than the node go in the left subtree
- Values greater than the node go in the right subtree

This ordering makes searching, inserting, and removing efficient when the tree stays balanced.

---

## Implementation

This binary search tree is implemented in Python using a `Node` class and a `BST` class.

File location:

```text
src/BinarySearchTree/BST
```

---

## Operations

| Operation | Description | Time Complexity |
|----------|-------------|-----------------|
| `insert(key)` | Adds a value to the tree | O(h) |
| `search(key)` | Returns the matching node or `None` | O(h) |
| `contains(key)` | Checks whether a value exists in the tree | O(h) |
| `find_min()` | Returns the smallest value or `None` | O(h) |
| `find_max()` | Returns the largest value or `None` | O(h) |
| `inorder_traversal()` | Returns values in sorted order | O(n) |
| `preorder_traversal()` | Returns values in root-left-right order | O(n) |
| `postorder_traversal()` | Returns values in left-right-root order | O(n) |
| `remove(key)` | Removes a value from the tree | O(h) |
| `is_empty()` | Checks if the tree has no root node | O(1) |
| `len(tree)` | Returns the number of values in the tree | O(n) |

`h` is the height of the tree. In a balanced tree, `h` is O(log n). In the worst case, `h` can be O(n).

---

## Example

```python
from importlib.machinery import SourceFileLoader

bst_module = SourceFileLoader(
    "bst_module",
    "src/BinarySearchTree/BST",
).load_module()

tree = bst_module.BST()

tree.insert(50)
tree.insert(30)
tree.insert(70)

print(tree.contains(30))           # True
print(tree.find_min())             # 30
print(tree.find_max())             # 70
print(tree.inorder_traversal())    # [30, 50, 70]
print(len(tree))                   # 3
```

---

## Common Uses

Binary search trees are used in:

- Fast lookup tables
- Sorted data storage
- Range queries
- Indexing systems
- Tree traversal practice

---

## Testing

Tests are located in:

```text
tests/TestsBinarySearchTree.py
```

Run tests with:

```bash
python tests/TestsBinarySearchTree.py
```

Or run the full test suite with:

```bash
pytest
```
