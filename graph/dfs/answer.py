# Implement your graph + traversals here

from dataclasses import dataclass
from typing import Self


@dataclass
class GraphNode:
    value: str
    neighbors: list[Self]


class Graph:
    def __init__(self):
        self._edges: dict[str, GraphNode] = {}

    def add_edge(self, u, v):
        # add new node to edge.
        self._add(u)
        self._add(v)

        # add neighbors each other.
        self._add_to_neighbor(u, v)
        self._add_to_neighbor(v, u)

    def _add(self, value: str):
        if value in self._edges:
            return
        self._edges[value] = GraphNode(value, [])

    def _validate_existance(self, node: str):
        if node not in self._edges:
            raise KeyError(f"{node=} does not exists")

    def _add_to_neighbor(self, me: str, new_neighbor: str):
        self._validate_existance(me)
        self._validate_existance(new_neighbor)

        # if exists, skip
        if any(e.value == new_neighbor for e in self._edges[me].neighbors):
            return
        self._edges[me].neighbors.append(self._edges[new_neighbor])

    def neighbors(self, node: str):
        self._validate_existance(node)
        return tuple(self._edges[node].neighbors)


def dfs(graph, start):
    results = []
    # Track visited per traversal so the same graph can be reused safely.
    visited = set()

    def search(node: str):
        if node not in visited:
            results.append(node)
            visited.add(node)

        for n in graph.neighbors(node):
            if n.value not in visited:
                search(n.value)

    search(start)
    return results
