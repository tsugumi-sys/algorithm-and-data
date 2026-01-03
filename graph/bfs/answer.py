# Implement your graph + traversals here

from dataclasses import dataclass
from typing import Any, Self


@dataclass
class GraphNode:
    value: str
    neighbors: list[Self]


class Graph:
    def __init__(self):
        self._edges: dict[str, GraphNode] = {}

    def add_edge(self, u, v):
        if u not in self._edges:
            new = GraphNode(u, [])
            self._edges[u] = new
        if v not in self._edges:
            new = GraphNode(v, [])
            self._edges[v] = new

        self._add_to_neighbor(u, v)
        self._add_to_neighbor(v, u)

    def _add_to_neighbor(self, node: str, new_neighbor: str):
        if any(
            n.value == new_neighbor for n in self._edges[node].neighbors
        ):  # avoid creating temporary list with any()
            return
        self._edges[node].neighbors.append(self._edges[new_neighbor])

    def neighbors(self, node: str) -> list[GraphNode]:
        return tuple(self._edges[node].neighbors)


@dataclass
class QueueNode:
    value: Any
    next: Self | None


class Queue:
    def __init__(self):
        self._head: QueueNode | None = None
        self._tail: QueueNode | None = None

    def enqueue(self, value: Any):
        new = QueueNode(value, None)
        if self._tail:
            self._tail.next = new
        else:
            self._head = new
        self._tail = new

    def dequeue(self) -> Any:
        if self._head is None:
            raise KeyError("queue is empty")

        poped = self._head
        self._head = poped.next

        if self._head is None:
            self._tail = None
        return poped.value

    def is_empty(self) -> bool:
        return self._head is None


def bfs(graph: Graph, start: str):
    queue = Queue()
    queue.enqueue(start)
    results = []
    # Track visited per traversal so the same graph can be reused safely.
    visited: set[str] = set()
    while not queue.is_empty():
        poped = queue.dequeue()
        if poped in visited:
            continue
        else:
            visited.add(poped)
            results.append(poped)

            for n in [n for n in graph.neighbors(poped) if n.value not in visited]:
                queue.enqueue(n.value)
    return results
