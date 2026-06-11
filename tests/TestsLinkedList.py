import sys
import unittest
from pathlib import Path

"""
Codex generated test cases for LinkedList class. Tests cover:
- Creating a new linked list and checking if it's empty.
- Appending, prepending, and inserting items into the list.
- Getting, finding, and setting item values.
- Removing items by index and by value.
- Clearing the list and confirming it's empty.
- Attempting invalid operations should raise IndexError or ValueError.

"""
ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from LinkedList.LinkedList import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_new_linked_list_is_empty(self):
        self.assertTrue(self.linked_list.is_empty())
        self.assertEqual(self.linked_list.size(), 0)
        self.assertEqual(self.linked_list.to_list(), [])
        self.assertEqual(str(self.linked_list), "")

    def test_append_adds_items_to_end(self):
        self.linked_list.append("first")
        self.linked_list.append("second")

        self.assertFalse(self.linked_list.is_empty())
        self.assertEqual(self.linked_list.size(), 2)
        self.assertEqual(self.linked_list.get(0), "first")
        self.assertEqual(self.linked_list.get(1), "second")
        self.assertEqual(self.linked_list.to_list(), ["first", "second"])
        self.assertEqual(str(self.linked_list), "first -> second")

    def test_prepend_adds_items_to_front(self):
        self.linked_list.prepend("second")
        self.linked_list.prepend("first")

        self.assertEqual(self.linked_list.size(), 2)
        self.assertEqual(self.linked_list.to_list(), ["first", "second"])
        self.assertEqual(str(self.linked_list), "first -> second")

    def test_insert_adds_items_at_index(self):
        self.linked_list.append("first")
        self.linked_list.append("third")

        self.linked_list.insert(1, "second")
        self.linked_list.insert(0, "zero")
        self.linked_list.insert(4, "fourth")

        self.assertEqual(self.linked_list.size(), 5)
        self.assertEqual(
            self.linked_list.to_list(),
            ["zero", "first", "second", "third", "fourth"],
        )

    def test_find_returns_first_matching_index(self):
        self.linked_list.append("a")
        self.linked_list.append("b")
        self.linked_list.append("a")

        self.assertEqual(self.linked_list.find("a"), 0)
        self.assertEqual(self.linked_list.find("b"), 1)

    def test_set_updates_item_at_index(self):
        self.linked_list.append("a")
        self.linked_list.append("b")

        self.linked_list.set(1, "changed")

        self.assertEqual(self.linked_list.get(1), "changed")
        self.assertEqual(self.linked_list.to_list(), ["a", "changed"])

    def test_remove_at_removes_items_by_index(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)

        self.linked_list.remove_at(1)
        self.linked_list.remove_at(0)

        self.assertEqual(self.linked_list.size(), 1)
        self.assertEqual(self.linked_list.to_list(), [3])

    def test_remove_deletes_first_matching_value(self):
        self.linked_list.append("a")
        self.linked_list.append("b")
        self.linked_list.append("a")

        self.linked_list.remove("a")

        self.assertEqual(self.linked_list.size(), 2)
        self.assertEqual(self.linked_list.to_list(), ["b", "a"])

    def test_clear_removes_all_items(self):
        self.linked_list.append("a")
        self.linked_list.append("b")

        self.linked_list.clear()

        self.assertTrue(self.linked_list.is_empty())
        self.assertEqual(self.linked_list.size(), 0)
        self.assertEqual(self.linked_list.to_list(), [])
        self.assertEqual(str(self.linked_list), "")

    def test_insert_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.linked_list.insert(-1, "bad")

        with self.assertRaises(IndexError):
            self.linked_list.insert(1, "bad")

    def test_get_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.linked_list.get(0)

        self.linked_list.append("value")

        with self.assertRaises(IndexError):
            self.linked_list.get(-1)

        with self.assertRaises(IndexError):
            self.linked_list.get(1)

    def test_set_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.linked_list.set(0, "bad")

        self.linked_list.append("value")

        with self.assertRaises(IndexError):
            self.linked_list.set(-1, "bad")

        with self.assertRaises(IndexError):
            self.linked_list.set(1, "bad")

    def test_remove_at_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.linked_list.remove_at(0)

        self.linked_list.append("value")

        with self.assertRaises(IndexError):
            self.linked_list.remove_at(-1)

        with self.assertRaises(IndexError):
            self.linked_list.remove_at(1)

    def test_find_missing_value_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.linked_list.find("missing")

    def test_remove_missing_value_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.linked_list.remove("missing")


if __name__ == "__main__":
    unittest.main()
