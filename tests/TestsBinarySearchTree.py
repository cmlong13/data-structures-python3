import sys
import unittest
from pathlib import Path

"""
Codex generated test cases for BST class. Tests cover:
- Creating a new binary search tree and checking if it's empty.
- Inserting values and confirming search, contains, and length behavior.
- Finding minimum and maximum values.
- Returning values in inorder, preorder, and postorder traversal order.
- Removing leaf nodes, nodes with one child, nodes with two children, and the root.
- Ignoring duplicate insertions and missing-value removals.
"""
ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from BinarySearchTree.BST import BST


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BST()

    def insert_values(self, values):
        for value in values:
            self.bst.insert(value)

    def test_new_tree_is_empty(self):
        self.assertTrue(self.bst.is_empty())
        self.assertEqual(len(self.bst), 0)
        self.assertIsNone(self.bst.find_min())
        self.assertIsNone(self.bst.find_max())
        self.assertEqual(self.bst.inorder_traversal(), [])
        self.assertEqual(self.bst.preorder_traversal(), [])
        self.assertEqual(self.bst.postorder_traversal(), [])

    def test_insert_adds_values_to_tree(self):
        self.insert_values([50, 30, 70])

        self.assertFalse(self.bst.is_empty())
        self.assertEqual(len(self.bst), 3)
        self.assertEqual(self.bst.root.val, 50)
        self.assertEqual(self.bst.root.left.val, 30)
        self.assertEqual(self.bst.root.right.val, 70)

    def test_search_returns_matching_node(self):
        self.insert_values([50, 30, 70, 20, 40, 60, 80])

        found = self.bst.search(40)

        self.assertIsNotNone(found)
        self.assertEqual(found.val, 40)
        self.assertIsNone(self.bst.search(100))

    def test_contains_returns_boolean_for_value_presence(self):
        self.insert_values([50, 30, 70])

        self.assertTrue(self.bst.contains(30))
        self.assertFalse(self.bst.contains(99))

    def test_duplicate_values_are_ignored(self):
        self.insert_values([50, 30, 70, 30, 50, 70])

        self.assertEqual(len(self.bst), 3)
        self.assertEqual(self.bst.inorder_traversal(), [30, 50, 70])

    def test_find_min_and_max_return_extreme_values(self):
        self.insert_values([50, 30, 70, 20, 40, 60, 80])

        self.assertEqual(self.bst.find_min(), 20)
        self.assertEqual(self.bst.find_max(), 80)

    def test_traversals_return_expected_orders(self):
        self.insert_values([50, 30, 70, 20, 40, 60, 80])

        self.assertEqual(
            self.bst.inorder_traversal(),
            [20, 30, 40, 50, 60, 70, 80],
        )
        self.assertEqual(
            self.bst.preorder_traversal(),
            [50, 30, 20, 40, 70, 60, 80],
        )
        self.assertEqual(
            self.bst.postorder_traversal(),
            [20, 40, 30, 60, 80, 70, 50],
        )

    def test_remove_leaf_node(self):
        self.insert_values([50, 30, 70, 20, 40, 60, 80])

        self.bst.remove(20)

        self.assertFalse(self.bst.contains(20))
        self.assertEqual(len(self.bst), 6)
        self.assertEqual(self.bst.inorder_traversal(), [30, 40, 50, 60, 70, 80])

    def test_remove_node_with_one_child(self):
        self.insert_values([50, 30, 70, 20])

        self.bst.remove(30)

        self.assertFalse(self.bst.contains(30))
        self.assertEqual(len(self.bst), 3)
        self.assertEqual(self.bst.inorder_traversal(), [20, 50, 70])

    def test_remove_node_with_two_children(self):
        self.insert_values([50, 30, 70, 20, 40, 60, 80])

        self.bst.remove(50)

        self.assertFalse(self.bst.contains(50))
        self.assertEqual(len(self.bst), 6)
        self.assertEqual(self.bst.inorder_traversal(), [20, 30, 40, 60, 70, 80])
        self.assertEqual(self.bst.root.val, 60)

    def test_remove_only_node_makes_tree_empty(self):
        self.bst.insert(10)

        self.bst.remove(10)

        self.assertTrue(self.bst.is_empty())
        self.assertEqual(len(self.bst), 0)
        self.assertEqual(self.bst.inorder_traversal(), [])

    def test_remove_missing_value_leaves_tree_unchanged(self):
        self.insert_values([50, 30, 70])

        self.bst.remove(999)

        self.assertEqual(len(self.bst), 3)
        self.assertEqual(self.bst.inorder_traversal(), [30, 50, 70])


if __name__ == "__main__":
    unittest.main()
