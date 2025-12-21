from dataclasses import dataclass
from typing import Self, Any


@dataclass
class Node:
    item: Any
    next: Self | None


class Stack:
    def __init__(self):
        raise NotImplementedError

    def pop(self) -> Any:
        raise NotImplementedError

    def push(self, item: Any):
        raise NotImplementedError

    def peek(self) -> Any:
        raise NotImplementedError

    def isEmpty(self):
        raise NotImplementedError
