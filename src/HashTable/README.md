# Hash Table

A **hash table** is a data structure that stores key-value pairs.

It uses a hash function to decide where each key should be stored, which makes lookup, insertion, and deletion fast on average.

---

## Implementation

This hash table is implemented in Python using a list of buckets and **separate chaining** for collisions.

File location:

```text
src/HashTable/HashTable.py
```

---

## Operations

| Operation | Description | Time Complexity |
|----------|-------------|-----------------|
| `set(key, value)` | Adds or updates a key-value pair | O(1) average, O(n) worst case |
| `get(key)` | Returns the value for a key | O(1) average, O(n) worst case |
| `remove(key)` | Removes a key-value pair and returns its value | O(1) average, O(n) worst case |
| `contains(key)` | Checks whether a key exists | O(1) average, O(n) worst case |
| `is_empty()` | Checks if the hash table is empty | O(1) |
| `size()` | Returns the number of key-value pairs | O(1) |
| `keys()` | Returns all keys | O(n) |
| `values()` | Returns all values | O(n) |
| `items()` | Returns all key-value pairs | O(n) |
| `clear()` | Removes all key-value pairs | O(n) |

---

## Example

```python
from src.HashTable.HashTable import HashTable

table = HashTable()

table.set("language", "Python")
table.set("version", 3)

print(table.get("language"))      # Python
print(table.contains("version"))  # True
print(table.size())               # 2

table.remove("version")
print(table.size())               # 1
```

You can also use dictionary-style access:

```python
table["topic"] = "data structures"
print(table["topic"])  # data structures
```

---

## Common Uses

Hash tables are used in:

- Dictionaries and maps
- Caches
- Database indexes
- Counting frequencies
- Fast membership checks

---

## Testing

Tests are located in:

```text
tests/test_hash_table.py
```

Run tests with pytest:

```bash
python -m pytest tests/test_hash_table.py
```
