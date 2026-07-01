import sys
import unittest
from pathlib import Path

"""
Codex generated test cases for DoublyLinkedList class. Tests cover:
- Creating a new doubly linked list and checking if it's empty.
- Appending, prepending, and inserting items into the list.
- Getting, finding, and setting item values.
- Removing items by index and by value.
- Traversing values forward and backward.
- Clearing the list and confirming it's empty.
- Attempting invalid operations should raise IndexError or ValueError.

"""
ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from DoublyLinkedList.DLL import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()

    def assert_links_are_consistent(self):
        current = self.dll.head
        previous = None

        while current:
            self.assertIs(current.prev, previous)
            previous = current
            current = current.next

        self.assertIs(previous, self.dll.tail)

        if self.dll.head:
            self.assertIsNone(self.dll.head.prev)
            self.assertIsNone(self.dll.tail.next)
        else:
            self.assertIsNone(self.dll.tail)

    def test_new_doubly_linked_list_is_empty(self):
        self.assertTrue(self.dll.is_empty())
        self.assertEqual(self.dll.size(), 0)
        self.assertEqual(self.dll.to_list(), [])
        self.assertEqual(self.dll.reverse_list(), [])
        self.assertEqual(str(self.dll), "")
        self.assert_links_are_consistent()

    def test_append_adds_items_to_end(self):
        self.dll.append("first")
        self.dll.append("second")

        self.assertFalse(self.dll.is_empty())
        self.assertEqual(self.dll.size(), 2)
        self.assertEqual(self.dll.get(0), "first")
        self.assertEqual(self.dll.get(1), "second")
        self.assertEqual(self.dll.to_list(), ["first", "second"])
        self.assertEqual(self.dll.reverse_list(), ["second", "first"])
        self.assertEqual(str(self.dll), "first <-> second")
        self.assert_links_are_consistent()

    def test_prepend_adds_items_to_front(self):
        self.dll.prepend("second")
        self.dll.prepend("first")

        self.assertEqual(self.dll.size(), 2)
        self.assertEqual(self.dll.to_list(), ["first", "second"])
        self.assertEqual(self.dll.reverse_list(), ["second", "first"])
        self.assertEqual(str(self.dll), "first <-> second")
        self.assert_links_are_consistent()

    def test_insert_adds_items_at_index(self):
        self.dll.append("first")
        self.dll.append("third")

        self.dll.insert(1, "second")
        self.dll.insert(0, "zero")
        self.dll.insert(4, "fourth")

        self.assertEqual(self.dll.size(), 5)
        self.assertEqual(
            self.dll.to_list(),
            ["zero", "first", "second", "third", "fourth"],
        )
        self.assertEqual(
            self.dll.reverse_list(),
            ["fourth", "third", "second", "first", "zero"],
        )
        self.assert_links_are_consistent()

    def test_find_returns_first_matching_index(self):
        self.dll.append("a")
        self.dll.append("b")
        self.dll.append("a")

        self.assertEqual(self.dll.find("a"), 0)
        self.assertEqual(self.dll.find("b"), 1)

    def test_set_updates_item_at_index(self):
        self.dll.append("a")
        self.dll.append("b")

        self.dll.set(1, "changed")

        self.assertEqual(self.dll.get(1), "changed")
        self.assertEqual(self.dll.to_list(), ["a", "changed"])
        self.assert_links_are_consistent()

    def test_remove_at_removes_items_by_index(self):
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.dll.append(4)

        self.dll.remove_at(1)
        self.dll.remove_at(2)
        self.dll.remove_at(0)

        self.assertEqual(self.dll.size(), 1)
        self.assertEqual(self.dll.to_list(), [3])
        self.assertEqual(self.dll.reverse_list(), [3])
        self.assert_links_are_consistent()

    def test_remove_deletes_first_matching_value(self):
        self.dll.append("a")
        self.dll.append("b")
        self.dll.append("a")

        self.dll.remove("a")

        self.assertEqual(self.dll.size(), 2)
        self.assertEqual(self.dll.to_list(), ["b", "a"])
        self.assertEqual(self.dll.reverse_list(), ["a", "b"])
        self.assert_links_are_consistent()

    def test_clear_removes_all_items(self):
        self.dll.append("a")
        self.dll.append("b")

        self.dll.clear()

        self.assertTrue(self.dll.is_empty())
        self.assertEqual(self.dll.size(), 0)
        self.assertEqual(self.dll.to_list(), [])
        self.assertEqual(self.dll.reverse_list(), [])
        self.assertEqual(str(self.dll), "")
        self.assert_links_are_consistent()

    def test_insert_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.dll.insert(-1, "bad")

        with self.assertRaises(IndexError):
            self.dll.insert(1, "bad")

    def test_get_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.dll.get(0)

        self.dll.append("value")

        with self.assertRaises(IndexError):
            self.dll.get(-1)

        with self.assertRaises(IndexError):
            self.dll.get(1)

    def test_set_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.dll.set(0, "bad")

        self.dll.append("value")

        with self.assertRaises(IndexError):
            self.dll.set(-1, "bad")

        with self.assertRaises(IndexError):
            self.dll.set(1, "bad")

    def test_remove_at_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.dll.remove_at(0)

        self.dll.append("value")

        with self.assertRaises(IndexError):
            self.dll.remove_at(-1)

        with self.assertRaises(IndexError):
            self.dll.remove_at(1)

    def test_find_missing_value_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.dll.find("missing")

    def test_remove_missing_value_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.dll.remove("missing")


if __name__ == "__main__":
    unittest.main()
