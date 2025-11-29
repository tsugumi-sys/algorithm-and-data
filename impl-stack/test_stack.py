import pytest
from stack import Stack


def test_new_stack_is_empty():
    """Test that a newly created stack is empty"""
    stack = Stack()
    assert stack.isEmpty() == True


def test_push_single_item():
    """Test pushing a single item onto the stack"""
    stack = Stack()
    stack.push(1)
    assert stack.isEmpty() == False


def test_push_multiple_items():
    """Test pushing multiple items onto the stack"""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.isEmpty() == False


def test_peek_returns_top_item():
    """Test that peek returns the top item without removing it"""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2
    assert stack.peek() == 2  # Should still be 2
    assert stack.isEmpty() == False  # Stack should still have items


def test_pop_single_item():
    """Test popping a single item from the stack"""
    stack = Stack()
    stack.push(1)
    result = stack.pop()
    assert result == 1
    assert stack.isEmpty() == True


def test_pop_multiple_items_lifo_order():
    """Test that pop returns items in LIFO (Last In First Out) order"""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.isEmpty() == True


def test_pop_from_empty_stack_raises_error():
    """Test that popping from an empty stack raises an exception"""
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()


def test_peek_from_empty_stack_raises_error():
    """Test that peeking at an empty stack raises an exception"""
    stack = Stack()
    with pytest.raises(IndexError):
        stack.peek()


def test_push_pop_push_sequence():
    """Test alternating push and pop operations"""
    stack = Stack()
    stack.push(1)
    assert stack.pop() == 1
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.isEmpty() == True


def test_push_different_data_types():
    """Test that stack can handle different data types"""
    stack = Stack()
    stack.push(1)
    stack.push("hello")
    stack.push([1, 2, 3])
    stack.push({"key": "value"})

    assert stack.pop() == {"key": "value"}
    assert stack.pop() == [1, 2, 3]
    assert stack.pop() == "hello"
    assert stack.pop() == 1


def test_peek_does_not_modify_stack():
    """Test that multiple peeks don't change the stack"""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    for _ in range(5):
        assert stack.peek() == 3

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_large_number_of_items():
    """Test stack with a large number of items"""
    stack = Stack()
    n = 1000
    for i in range(n):
        stack.push(i)

    for i in range(n - 1, -1, -1):
        assert stack.pop() == i

    assert stack.isEmpty() == True


def test_push_none_value():
    """Test that None can be pushed onto the stack"""
    stack = Stack()
    stack.push(None)
    assert stack.isEmpty() == False
    assert stack.peek() is None
    assert stack.pop() is None


def test_push_zero():
    """Test that zero can be pushed onto the stack"""
    stack = Stack()
    stack.push(0)
    assert stack.isEmpty() == False
    assert stack.peek() == 0
    assert stack.pop() == 0


def test_isEmpty_after_operations():
    """Test isEmpty returns correct value after various operations"""
    stack = Stack()
    assert stack.isEmpty() == True

    stack.push(1)
    assert stack.isEmpty() == False

    stack.push(2)
    assert stack.isEmpty() == False

    stack.pop()
    assert stack.isEmpty() == False

    stack.pop()
    assert stack.isEmpty() == True
