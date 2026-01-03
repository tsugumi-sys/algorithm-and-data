from dataclasses import dataclass
from typing import Any, Self


@dataclass
class Node:
    value: Any
    next: Self | None
    prev: Self | None


class DoublyLinkedList:
    def __init__(self):
        self._head: Node | None = None
        self._tail: Node | None = None
        self._size = 0

    def append(self, value):
        new = Node(value, None, None)
        if self._head is None and self._tail is None:
            self._head = new
            self._tail = new
        else:
            tail = self._tail
            tail.next = new
            new.prev = tail
            self._tail = new
        self._size += 1

    def prepend(self, value):
        new = Node(value, None, None)
        if self._head is None and self._tail is None:
            self._head = new
            self._tail = new
        else:
            head = self._head
            head.prev = new
            new.next = head
            self._head = new
        self._size += 1

    def insert(self, index, value):
        if index > self._size or index < 0:  # zero based position.
            raise IndexError

        # head or single node case.
        if self._size == 1 or index == 0:
            self.prepend(value)  # handle adding as a head.
        # multiple node and not-head case.
        elif index == self._size:
            self.append(value)
        else:
            new = Node(value, None, None)
            # if index is tail, we add new node to before the current tail, so we don't need to update the tail pointer.
            node = self._head
            current_idx = 0
            while node:
                if current_idx == index:
                    break
                node = node.next
                current_idx += 1

            node.prev.next = new
            new.prev = node.prev

            node.prev = new
            new.next = node

            self._size += 1

    def pop_first(self):
        if self._size == 0:
            raise IndexError
        poped = self._head
        if self._size == 1:
            self._head = None
            self._tail = None
        else:
            new_head = poped.next
            new_head.prev = None
            self._head = new_head

        self._size -= 1
        return poped.value

    def pop_last(self):
        if self._size == 0:
            raise IndexError
        poped = self._tail
        if self._size == 1:
            self._head = None
            self._tail = None
        else:
            new_tail = poped.prev
            new_tail.next = None
            self._tail = new_tail

        self._size -= 1
        return poped.value

    def find(self, value):
        current_node = self._head
        found = False
        while current_node:
            if value == current_node.value:
                found = True
                break
            current_node = current_node.next
        return found

    def iter_reverse(self):
        reversed_items = []
        current = self._tail
        while current:
            reversed_items.append(current.value)
            current = current.prev
        return reversed_items

    def __len__(self):
        return self._size

    def __iter__(self):
        current = self._head
        while current:
            yield current.value
            current = current.next
