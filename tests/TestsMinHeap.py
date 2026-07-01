import sys
import unittest
from pathlib import Path

"""
Codex generated test cases for MinHeap class. Tests cover:
- Creating a new heap and checking if it is empty.
- Inserting values and confirming the smallest value moves to the root.
- Peeking at the smallest value without removing it.
- Removing values in ascending order.
- Handling duplicate, negative, single, and empty values.
"""
ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from Heaps.MinHeap import MinHeap


class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.heap = MinHeap()

    def insert_values(self, values):
        for value in values:
            self.heap.insert(value)

    def assert_valid_min_heap(self):
        for index, value in enumerate(self.heap.heap):
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2

            if left_child_index < len(self.heap.heap):
                self.assertLessEqual(value, self.heap.heap[left_child_index])
            if right_child_index < len(self.heap.heap):
                self.assertLessEqual(value, self.heap.heap[right_child_index])

    def test_new_heap_is_empty(self):
        self.assertTrue(self.heap.is_empty())
        self.assertEqual(len(self.heap), 0)
        self.assertIsNone(self.heap.peek())
        self.assertIsNone(self.heap.remove_min())

    def test_insert_adds_values_and_keeps_smallest_at_root(self):
        self.insert_values([30, 10, 20, 5])

        self.assertFalse(self.heap.is_empty())
        self.assertEqual(len(self.heap), 4)
        self.assertEqual(self.heap.peek(), 5)
        self.assert_valid_min_heap()

    def test_peek_does_not_remove_value(self):
        self.insert_values([7, 3, 9])

        self.assertEqual(self.heap.peek(), 3)
        self.assertEqual(self.heap.peek(), 3)
        self.assertEqual(len(self.heap), 3)

    def test_remove_min_returns_values_in_ascending_order(self):
        values = [12, 3, 17, 8, 1, 25, 5]
        self.insert_values(values)

        removed_values = [self.heap.remove_min() for _ in values]

        self.assertEqual(removed_values, sorted(values))
        self.assertTrue(self.heap.is_empty())
        self.assertEqual(len(self.heap), 0)

    def test_remove_min_restores_heap_property_after_each_removal(self):
        self.insert_values([40, 15, 30, 10, 20, 5])

        while not self.heap.is_empty():
            self.heap.remove_min()
            self.assert_valid_min_heap()

    def test_duplicate_and_negative_values_are_supported(self):
        values = [4, -1, 4, -3, 0, -1]
        self.insert_values(values)

        removed_values = [self.heap.remove_min() for _ in values]

        self.assertEqual(removed_values, sorted(values))

    def test_remove_min_single_value_empties_heap(self):
        self.heap.insert(42)

        self.assertEqual(self.heap.remove_min(), 42)
        self.assertTrue(self.heap.is_empty())
        self.assertIsNone(self.heap.peek())


if __name__ == "__main__":
    unittest.main()
