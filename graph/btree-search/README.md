Scenario

Imagine a simple database index implemented as a binary search tree (BST). An in-order traversal returns the indexed rows sorted by key, pre-order can serialize the tree for storage, and post-order can help with cleanup (e.g., deleting nodes safely).

Interface

    class Node:
        value: the key stored at this node
        left: left child or None
        right: right child or None

    class BinarySearchTree:
        insert(value): add value into the BST (duplicates go to the right subtree)
        search(value): return True if value exists in the tree, else False
        remove(value): remove one occurrence of value, raising KeyError if value not found
        preorder(): return a list of values in pre-order (root, left, right)
        inorder(): return a list of values in in-order (left, root, right)
        postorder(): return a list of values in post-order (left, right, root)

Behavior

- Start with an empty tree. Traversals on an empty tree return an empty list.
- Maintain BST ordering on insert; duplicates are allowed and placed in the right subtree.
- remove(value) deletes exactly one matching node while preserving BST ordering; if the value is not present raise KeyError.
- Traversal results should be deterministic and reflect the current tree structure.
Implement everything in `main.py`.
