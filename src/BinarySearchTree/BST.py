class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None
    
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_rec(node.left, key)
        elif key > node.val:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_rec(node.right, key)

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search_rec(node.left, key)
        return self._search_rec(node.right, key)
    
    def contains(self, key):
        return self.search(key) is not None
    
    def find_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.val

    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.val
    
    def inorder_traversal(self):
        result = []
        self._inorder_rec(self.root, result)
        return result
    
    def _inorder_rec(self, node, result):
        if node:
            self._inorder_rec(node.left, result)
            result.append(node.val)
            self._inorder_rec(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_rec(self.root, result)
        return result
    
    def _preorder_rec(self, node, result):
        if node:
            result.append(node.val)
            self._preorder_rec(node.left, result)
            self._preorder_rec(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_rec(self.root, result)
        return result
    
    def _postorder_rec(self, node, result):
        if node:
            self._postorder_rec(node.left, result)
            self._postorder_rec(node.right, result)
            result.append(node.val)

    def remove(self, key):
        self.root = self._remove_rec(self.root, key)

    def _remove_rec(self, node, key):
        if node is None:
            return node
        
        if key < node.val:
            node.left = self._remove_rec(node.left, key)
        elif key > node.val:
            node.right = self._remove_rec(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self._find_min_node(node.right)
            node.val = temp.val
            node.right = self._remove_rec(node.right, temp.val)
        
        return node
    
    def _find_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def __len__(self):
        return self._size_rec(self.root)
    
    def _size_rec(self, node):
        if node is None:
            return 0
        return 1 + self._size_rec(node.left) + self._size_rec(node.right)
    
