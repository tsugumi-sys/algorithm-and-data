import pytest

from main import LinkedList


def make_list(values=()):
    """Helper to create a list with the given values appended in order."""
    ll = LinkedList()
    for value in values:
        ll.append(value)
    return ll


def test_new_list_is_empty():
    ll = LinkedList()
    assert len(ll) == 0
    assert list(ll) == []


def test_append_adds_to_tail():
    ll = make_list([1, 2, 3])
    assert len(ll) == 3
    assert list(ll) == [1, 2, 3]


def test_prepend_updates_head():
    ll = make_list([2, 3])
    ll.prepend(1)
    assert list(ll) == [1, 2, 3]
    assert len(ll) == 3


def test_insert_handles_start_middle_and_end():
    ll = make_list([1, 3])
    ll.insert(1, 2)
    assert list(ll) == [1, 2, 3]

    ll.insert(0, 0)
    assert list(ll) == [0, 1, 2, 3]

    ll.insert(len(ll), 4)
    assert list(ll) == [0, 1, 2, 3, 4]


def test_insert_out_of_bounds_raises():
    ll = make_list([1, 2])
    with pytest.raises(IndexError):
        ll.insert(5, 99)
    with pytest.raises(IndexError):
        ll.insert(-1, 99)


def test_pop_first_removes_head():
    ll = make_list([1, 2, 3])
    assert ll.pop_first() == 1
    assert list(ll) == [2, 3]
    assert len(ll) == 2

    assert ll.pop_first() == 2
    assert ll.pop_first() == 3
    with pytest.raises(IndexError):
        ll.pop_first()


def test_pop_last_removes_tail():
    ll = make_list([1, 2, 3])
    assert ll.pop_last() == 3
    assert list(ll) == [1, 2]
    assert len(ll) == 2

    assert ll.pop_last() == 2
    assert ll.pop_last() == 1
    with pytest.raises(IndexError):
        ll.pop_last()


def test_find_reports_membership():
    ll = make_list(["a", None, "c"])
    assert ll.find("a") is True
    assert ll.find(None) is True
    assert ll.find("missing") is False


def test_iteration_tracks_mutations():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.prepend(0)
    ll.insert(2, 1.5)
    assert list(ll) == [0, 1, 1.5, 2]

    ll.pop_first()
    ll.pop_last()
    assert list(ll) == [1, 1.5]
