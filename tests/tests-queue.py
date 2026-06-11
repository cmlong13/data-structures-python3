import sys
import unittest
import importlib.util
from pathlib import Path

"""
Codex generated test cases for Queue class. Tests cover:
- Creating a new queue and checking if it's empty.
- Enqueueing items onto the queue and verifying the front item and size.
- Dequeueing items from the queue and ensuring they come off in FIFO order.
- Peeking at the front item without removing it.
- Clearing the queue and confirming it's empty.
- Attempting to dequeue or peek from an empty queue should raise an IndexError.

"""
ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

QUEUE_PATH = SRC_DIR / "queue" / "queue.py"
QUEUE_SPEC = importlib.util.spec_from_file_location("queue_module", QUEUE_PATH)
QUEUE_MODULE = importlib.util.module_from_spec(QUEUE_SPEC)
QUEUE_SPEC.loader.exec_module(QUEUE_MODULE)
queue = QUEUE_MODULE.queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = queue()

    def test_new_queue_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 0)
        self.assertEqual(str(self.queue), "[]")

    def test_enqueue_adds_items_to_back(self):
        self.queue.enqueue("first")
        self.queue.enqueue("second")

        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 2)
        self.assertEqual(self.queue.peek(), "first")
        self.assertEqual(str(self.queue), "['first', 'second']")

    def test_dequeue_removes_items_in_fifo_order(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 0)

    def test_peek_does_not_remove_item(self):
        self.queue.enqueue("front")

        self.assertEqual(self.queue.peek(), "front")
        self.assertEqual(self.queue.peek(), "front")
        self.assertEqual(self.queue.size(), 1)

    def test_clear_removes_all_items(self):
        self.queue.enqueue("a")
        self.queue.enqueue("b")

        self.queue.clear()

        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 0)
        self.assertEqual(str(self.queue), "[]")

    def test_dequeue_empty_queue_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_peek_empty_queue_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.queue.peek()


if __name__ == "__main__":
    unittest.main()
