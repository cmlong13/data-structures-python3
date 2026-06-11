import sys
import unittest
from pathlib import Path

"""
Codex generated test cases for Stack class. Tests cover:
- Creating a new stack and checking if it's empty.  
- Pushing items onto the stack and verifying the top item and size.
- Popping items from the stack and ensuring they come off in LIFO order.
- Peeking at the top item without removing it.
- Clearing the stack and confirming it's empty.
- Attempting to pop or peek from an empty stack should raise an IndexError.

"""
ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from stack.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_new_stack_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)
        self.assertEqual(str(self.stack), "[]")

    def test_push_adds_items_to_top(self):
        self.stack.push("first")
        self.stack.push("second")

        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 2)
        self.assertEqual(self.stack.peek(), "second")
        self.assertEqual(str(self.stack), "['first', 'second']")

    def test_pop_removes_items_in_lifo_order(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)

    def test_peek_does_not_remove_item(self):
        self.stack.push("top")

        self.assertEqual(self.stack.peek(), "top")
        self.assertEqual(self.stack.peek(), "top")
        self.assertEqual(self.stack.size(), 1)

    def test_clear_removes_all_items(self):
        self.stack.push("a")
        self.stack.push("b")

        self.stack.clear()

        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)
        self.assertEqual(str(self.stack), "[]")

    def test_pop_empty_stack_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek_empty_stack_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.stack.peek()


if __name__ == "__main__":
    unittest.main()