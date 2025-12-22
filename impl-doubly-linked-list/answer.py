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

    def _insert_between(self, prev: Node | None, new_node: Node, next: Node | None):
        if prev:
            prev.next = new_node
            new_node.prev = prev
        else:
            self._head = new_node
        if next:
            next.prev = new_node
            new_node.next = next
        else:
            self._tail = new_node
        self._size += 1

    def append(self, value):
        new = Node(value, None, None)
        self._insert_between(self._tail, new, None)

    def prepend(self, value):
        new = Node(value, None, None)
        self._insert_between(None, new, self._head)

    def insert(self, index, value):
        if index > self._size or index < 0:  # zero based position.
            raise IndexError

        new = Node(value, None, None)
        if index == 0:
            self._insert_between(None, new, self._head)
        elif index == self._size:
            self._insert_between(self._tail, new, None)  # handle adding as a head.
        else:
            # if index is tail, we add new node to before the current tail, so we don't need to update the tail pointer.
            node = self._head
            current_idx = 0
            while node:
                if current_idx == index:
                    break
                node = node.next
                current_idx += 1
            self._insert_between(node.prev, new, node)

    def _remove(self, node: Node):
        if node is None:
            raise IndexError

        if node.prev:
            node.prev.next = node.next
        else:
            self._head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self._tail = node.prev
        self._size -= 1
        return node.value

    def pop_first(self):
        if self._size == 0:
            raise IndexError
        poped = self._remove(self._head)
        return poped

    def pop_last(self):
        if self._size == 0:
            raise IndexError
        poped = self._remove(self._tail)
        return poped

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
        current = self._tail
        while current:
            yield current.value
            current = current.prev

    def __len__(self):
        return self._size

    def __iter__(self):
        current = self._head
        while current:
            yield current.value
            current = current.next
