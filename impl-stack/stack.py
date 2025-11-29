from dataclasses import dataclass
from typing import Self, Any


@dataclass
class Node:
    item: Any
    next: Self | None


class Stack:
    def __init__(self):
        self._head: Node | None = None

    def pop(self) -> Any:
        head = self._head
        if head is None:
            raise IndexError()
        self._head = head.next
        return head.item

    def push(self, item: Any):
        node = Node(item, None)
        head = self._head
        if head is None:
            self._head = node
            return
        node.next = head
        self._head = node

    def peek(self) -> Any:
        head = self._head
        if head is None:
            raise IndexError()
        return head.item

    def isEmpty(self):
        return self._head is None
