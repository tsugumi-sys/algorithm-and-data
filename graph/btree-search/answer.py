# Implement your BST here
from typing import Self, Any


class Node:
    def __init__(self, value):
        self._value = value
        self._right: Self | None = None
        self._left: Self | None = None

    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def right(self) -> Self | None:
        return self._right

    @right.setter
    def right(self, node: Self | None) -> Any:
        self._right = node

    @property
    def left(self) -> Self | None:
        return self._left

    @left.setter
    def left(self, node: Self | None) -> Any:
        self._left = node

    def __repr__(self):
        return f"Node(value={self.value})"


class BinarySearchTree:
    def __init__(self):
        self._root: Node | None = None

    def insert(self, value):
        """
        1. If root is none, use it.
        2. if not None, compare the root, if the new value is greater (smaller) than the current node, go right (left). If it's equal, go right.
        3. if you find a place to add, add to leaf, if the node is not a leaf, if it has not a leaf, swap with the new node, and add to left or right.
        """
        new_node = Node(value)
        if self._root is None:
            self._root = new_node
            return

        current_node = self._root
        while current_node:
            if new_node.value >= current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break
            else:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break

    def remove(self, value):
        def _min_node(root: Node) -> Node:
            while root.left:
                root = root.left
            return root

        def _delete(root: Node | None, value) -> Node:
            if not root:
                raise KeyError("Data not found")
            if value > root.value:
                root.right = _delete(root.right, value)
            elif value < root.value:
                root.left = _delete(root.left, value)
            else:
                if root.right is None:
                    return root.left
                if root.left is None:
                    return root.right

                # 2 children case
                successor = _min_node(root.right)
                root.value = successor.value
                root.right = _delete(root.right, successor.value)
            return root

        self._root = _delete(self._root, value)

    def search(self, value):
        current = self._root
        while current:
            if value > current.value:
                current = current.right
            elif value < current.value:
                current = current.left
            else:
                return True
        return False

    def preorder(self):
        results = []

        def _preorder_traversal(node: Node):
            if node is not None:
                results.append(node.value)
                _preorder_traversal(node.left)
                _preorder_traversal(node.right)

        _preorder_traversal(self._root)
        return results

    def inorder(self):
        """
        Search items
        1. left first.
        2. root.
        3. right after.
        """
        results = []

        def inorder_traversal(node: Node):
            if node is not None:
                inorder_traversal(node.left)
                results.append(node.value)
                inorder_traversal(node.right)

        inorder_traversal(self._root)
        return results

    def postorder(self):
        results = []

        def _postorder_traversal(node: Node):
            if node is not None:
                _postorder_traversal(node.left)
                _postorder_traversal(node.right)
                results.append(node.value)

        _postorder_traversal(self._root)
        return results
