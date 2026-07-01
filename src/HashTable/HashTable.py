class HashTable:
    """
    A simple hash table implementation using separate chaining.

    The table stores key-value pairs in buckets. Collisions are handled by
    keeping multiple pairs in the same bucket.
    """

    def __init__(self, capacity=8):
        if capacity <= 0:
            raise ValueError("capacity must be greater than zero")

        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
        self._size = 0

    def _bucket_index(self, key):
        return hash(key) % self.capacity

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def set(self, key, value):
        bucket = self.buckets[self._bucket_index(key)]

        for index, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[index] = (key, value)
                return

        bucket.append((key, value))
        self._size += 1

    def get(self, key):
        bucket = self.buckets[self._bucket_index(key)]

        for existing_key, value in bucket:
            if existing_key == key:
                return value

        raise KeyError("key not found")

    def remove(self, key):
        bucket = self.buckets[self._bucket_index(key)]

        for index, (existing_key, value) in enumerate(bucket):
            if existing_key == key:
                bucket.pop(index)
                self._size -= 1
                return value

        raise KeyError("key not found")

    def contains(self, key):
        bucket = self.buckets[self._bucket_index(key)]
        return any(existing_key == key for existing_key, _ in bucket)

    def keys(self):
        return [key for bucket in self.buckets for key, _ in bucket]

    def values(self):
        return [value for bucket in self.buckets for _, value in bucket]

    def items(self):
        return [item for bucket in self.buckets for item in bucket]

    def clear(self):
        self.buckets = [[] for _ in range(self.capacity)]
        self._size = 0

    def __contains__(self, key):
        return self.contains(key)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)

    def __delitem__(self, key):
        self.remove(key)

    def __str__(self):
        return str(dict(self.items()))
