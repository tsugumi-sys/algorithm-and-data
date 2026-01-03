import pytest

from main import DoublyLinkedList


def make_list(values=()):
    dll = DoublyLinkedList()
    for value in values:
        dll.append(value)
    return dll


def forward_values(dll):
    return list(dll)


def reverse_values(dll):
    return list(dll.iter_reverse())


def test_new_list_is_empty_and_iterates_both_ways():
    dll = DoublyLinkedList()
    assert len(dll) == 0
    assert forward_values(dll) == []
    assert reverse_values(dll) == []


def test_append_and_reverse_iteration():
    dll = make_list([1, 2, 3])
    assert forward_values(dll) == [1, 2, 3]
    assert reverse_values(dll) == [3, 2, 1]
    assert len(dll) == 3


def test_prepend_updates_head_and_tail():
    dll = make_list([2, 3])
    dll.prepend(1)
    assert forward_values(dll) == [1, 2, 3]
    assert reverse_values(dll) == [3, 2, 1]


def test_insert_middle_and_edges():
    dll = make_list([1, 3])
    dll.insert(1, 2)
    assert forward_values(dll) == [1, 2, 3]
    assert reverse_values(dll) == [3, 2, 1]

    dll.insert(0, 0)
    dll.append(4)
    assert forward_values(dll) == [0, 1, 2, 3, 4]
    assert reverse_values(dll) == [4, 3, 2, 1, 0]


def test_insert_out_of_bounds_raises():
    dll = make_list([1])
    with pytest.raises(IndexError):
        dll.insert(-1, 0)
    with pytest.raises(IndexError):
        dll.insert(2, 99)


def test_insert_at_len_appends():
    dll = make_list([1, 2])
    dll.insert(len(dll), 3)
    assert forward_values(dll) == [1, 2, 3]
    assert reverse_values(dll) == [3, 2, 1]


def test_pop_first_and_pop_last():
    dll = make_list([1, 2, 3])
    assert dll.pop_first() == 1
    assert dll.pop_last() == 3
    assert forward_values(dll) == [2]
    assert reverse_values(dll) == [2]
    assert len(dll) == 1

    assert dll.pop_first() == 2
    with pytest.raises(IndexError):
        dll.pop_first()
    with pytest.raises(IndexError):
        dll.pop_last()


def test_find_reports_membership():
    dll = make_list(["start", None, "end"])
    assert dll.find("start") is True
    assert dll.find(None) is True
    assert dll.find("missing") is False


def test_reverse_iteration_stays_valid_after_mutations():
    dll = make_list([1, 2, 3, 4])
    dll.pop_first()  # remove 1
    dll.pop_last()  # remove 4
    dll.prepend(0)
    dll.insert(2, 2.5)

    assert forward_values(dll) == [0, 2, 2.5, 3]
    assert reverse_values(dll) == [3, 2.5, 2, 0]
