import pytest
from queue import Queue


def test_new_queue_is_empty():
    """Test that a newly created queue is empty"""
    queue = Queue()
    assert queue.isEmpty() == True


def test_enqueue_single_item():
    """Test enqueueing a single item"""
    queue = Queue()
    queue.enqueue(1)
    assert queue.isEmpty() == False


def test_enqueue_multiple_items():
    """Test enqueueing multiple items"""
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.isEmpty() == False


def test_peek_returns_front_item():
    """Test that peek returns the front item without removing it"""
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.peek() == 1
    assert queue.peek() == 1  # Should still be 1
    assert queue.isEmpty() == False  # Queue should still have items


def test_dequeue_single_item():
    """Test dequeueing a single item"""
    queue = Queue()
    queue.enqueue(1)
    result = queue.dequeue()
    assert result == 1
    assert queue.isEmpty() == True


def test_dequeue_multiple_items_fifo_order():
    """Test that dequeue returns items in FIFO (First In First Out) order"""
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.isEmpty() == True


def test_dequeue_from_empty_queue_raises_error():
    """Test that dequeueing from an empty queue raises an exception"""
    queue = Queue()
    with pytest.raises(IndexError):
        queue.dequeue()


def test_peek_from_empty_queue_raises_error():
    """Test that peeking at an empty queue raises an exception"""
    queue = Queue()
    with pytest.raises(IndexError):
        queue.peek()


def test_enqueue_dequeue_enqueue_sequence():
    """Test alternating enqueue and dequeue operations"""
    queue = Queue()
    queue.enqueue(1)
    assert queue.dequeue() == 1
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.isEmpty() == True


def test_enqueue_different_data_types():
    """Test that queue can handle different data types"""
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue("hello")
    queue.enqueue([1, 2, 3])
    queue.enqueue({"key": "value"})

    assert queue.dequeue() == 1
    assert queue.dequeue() == "hello"
    assert queue.dequeue() == [1, 2, 3]
    assert queue.dequeue() == {"key": "value"}


def test_peek_does_not_modify_queue():
    """Test that multiple peeks don't change the queue"""
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    for _ in range(5):
        assert queue.peek() == 1

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3


def test_large_number_of_items():
    """Test queue with a large number of items"""
    queue = Queue()
    n = 1000
    for i in range(n):
        queue.enqueue(i)

    for i in range(n):
        assert queue.dequeue() == i

    assert queue.isEmpty() == True


def test_enqueue_none_value():
    """Test that None can be enqueued"""
    queue = Queue()
    queue.enqueue(None)
    assert queue.isEmpty() == False
    assert queue.peek() is None
    assert queue.dequeue() is None


def test_enqueue_zero():
    """Test that zero can be enqueued"""
    queue = Queue()
    queue.enqueue(0)
    assert queue.isEmpty() == False
    assert queue.peek() == 0
    assert queue.dequeue() == 0


def test_isEmpty_after_operations():
    """Test isEmpty returns correct value after various operations"""
    queue = Queue()
    assert queue.isEmpty() == True

    queue.enqueue(1)
    assert queue.isEmpty() == False

    queue.enqueue(2)
    assert queue.isEmpty() == False

    queue.dequeue()
    assert queue.isEmpty() == False

    queue.dequeue()
    assert queue.isEmpty() == True


def test_fifo_with_mixed_operations():
    """Test FIFO behavior with mixed enqueue and dequeue operations"""
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    queue.enqueue(3)
    queue.enqueue(4)
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    queue.enqueue(5)
    assert queue.dequeue() == 4
    assert queue.dequeue() == 5
    assert queue.isEmpty() == True
