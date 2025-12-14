import pytest

from main import BinarySearchTree


def build_tree(values):
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree


def test_inorder_returns_sorted_values_like_index_scan():
    values = [50, 30, 70, 20, 40, 60, 80, 70]
    tree = build_tree(values)
    assert tree.inorder() == sorted(values)


def test_preorder_serializes_structure_root_left_right():
    tree = build_tree([10, 5, 2, 7, 15, 12, 20])
    assert tree.preorder() == [10, 5, 2, 7, 15, 12, 20]


def test_postorder_visits_left_right_root():
    tree = build_tree([8, 3, 10, 1, 6, 14, 4, 7, 13])
    assert tree.postorder() == [1, 4, 7, 6, 3, 13, 14, 10, 8]


def test_search_finds_existing_and_missing_keys():
    tree = build_tree([5, 3, 7, 3, 9])
    assert tree.search(7) is True
    assert tree.search(3) is True  # duplicate present
    assert tree.search(8) is False


def test_traversals_on_empty_tree_return_empty_lists():
    tree = BinarySearchTree()
    assert tree.preorder() == []
    assert tree.inorder() == []
    assert tree.postorder() == []


def test_duplicates_go_to_right_subtree_and_appear_in_order():
    tree = build_tree([5, 5, 5])
    assert tree.preorder() == [5, 5, 5]
    assert tree.inorder() == [5, 5, 5]
    assert tree.postorder() == [5, 5, 5]


def test_inorder_supports_range_like_queries():
    values = [40, 20, 60, 10, 30, 50, 70, 65]
    tree = build_tree(values)
    # simulate pulling rows where 25 <= key <= 65
    inorder_values = tree.inorder()
    range_values = [v for v in inorder_values if 25 <= v <= 65]
    assert range_values == [30, 40, 50, 60, 65]
