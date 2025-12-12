import pytest

from main import MaxHeap, MinHeap


def drain(heap):
    values = []
    while not heap.is_empty():
        values.append(heap.pop())
    return values


def test_min_heap_orders_values_and_handles_duplicates():
    heap = MinHeap()
    for value in [5, 3, 8, 1, 3, -2]:
        heap.push(value)

    assert len(heap) == 6
    assert heap.peek() == -2
    assert drain(heap) == [-2, 1, 3, 3, 5, 8]
    assert heap.is_empty() is True


def test_max_heap_orders_values_and_handles_duplicates():
    heap = MaxHeap()
    for value in [5, 3, 8, 1, 3, -2]:
        heap.push(value)

    assert len(heap) == 6
    assert heap.peek() == 8
    assert drain(heap) == [8, 5, 3, 3, 1, -2]
    assert heap.is_empty() is True


def test_init_with_iterable_builds_valid_heaps():
    min_heap = MinHeap([7, 2, 9, 4])
    max_heap = MaxHeap([7, 2, 9, 4])

    assert len(min_heap) == 4
    assert len(max_heap) == 4

    assert drain(min_heap) == [2, 4, 7, 9]
    assert drain(max_heap) == [9, 7, 4, 2]


def test_peek_does_not_remove_items():
    heap = MinHeap([10, 5, 7])
    top = heap.peek()
    assert top == 5
    assert len(heap) == 3
    assert heap.pop() == 5
    assert heap.peek() == 7


def test_interleaved_operations_maintain_heap_property():
    heap = MinHeap()
    heap.push(10)
    heap.push(4)
    heap.push(7)
    assert heap.pop() == 4

    heap.push(3)
    heap.push(9)
    assert heap.peek() == 3
    assert heap.pop() == 3
    assert heap.pop() == 7

    heap.push(1)
    heap.push(6)
    assert drain(heap) == [1, 6, 9, 10]


def test_length_and_is_empty_track_state():
    heap = MaxHeap()
    assert heap.is_empty() is True
    assert len(heap) == 0

    for i in range(5):
        heap.push(i)
        assert len(heap) == i + 1
        assert heap.is_empty() is False

    for expected_length in range(5, 0, -1):
        assert len(heap) == expected_length
        heap.pop()
    assert heap.is_empty() is True
    assert len(heap) == 0


@pytest.mark.parametrize("HeapClass", [MinHeap, MaxHeap])
def test_pop_and_peek_on_empty_raise(HeapClass):
    heap = HeapClass()
    with pytest.raises(IndexError):
        heap.pop()
    with pytest.raises(IndexError):
        heap.peek()
