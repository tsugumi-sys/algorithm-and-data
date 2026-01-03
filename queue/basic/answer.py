from dataclasses import dataclass
from typing import Self


@dataclass
class QueueNode:
    value: any
    next: None | Self = None


class Queue:
    """
    Queue implementation using a linked list.

    Interface:
    - enqueue(item): Add an item to the back of the queue
    - dequeue(): Remove and return the item at the front of the queue
    - peek(): Return the item at the front of the queue without removing it
    - isEmpty(): Return True if the queue is empty, False otherwise
    """

    def __init__(self, capacity: int = 5):
        # TODO: Initialize your queue here
        if capacity < 0:
            raise ValueError("capacity must be greater than zero.")
        self._capacity = capacity
        self._size = 0
        self._head = None
        self._tail = None

    def enqueue(self, item):
        """Add an item to the back of the queue"""
        if self._size == self._capacity:
            raise OverflowError()
        self._add_to_end(QueueNode(item))

    def _add_to_end(self, new: QueueNode):
        if self._size == 0:
            self._head = new
            self._tail = new
            self._size += 1
            return
        # first, we need to move the head because we need to add the item.
        tail = self._tail
        tail.next = new
        self._tail = new
        self._size += 1

    def dequeue(self):
        """Remove and return the item at the front of the queue

        Raises:
            IndexError: If the queue is empty
        """
        if self.isEmpty():
            raise IndexError()
        if self._size == 1:
            node = self._head
            self._head = None
            self._tail = None
            self._size -= 1
            return node.value
        head = self._head
        self._head = head.next
        self._size -= 1
        return head.value

    def peek(self):
        """Return the item at the front of the queue without removing it

        Raises:
            IndexError: If the queue is empty
        """
        if self.isEmpty():
            raise IndexError()
        return self._head.value

    def isEmpty(self):
        """Return True if the queue is empty, False otherwise"""
        return self._size == 0

    @property
    def size(self) -> int:
        return self._size
