# Implement your graph + bidirectional search here
# Complexity discussion:
# - Let b be branching factor and d be shortest-path distance.
# - Single-source BFS expands O(b^0 + ... + b^d) = O(b^d) nodes and space.
# - Bidirectional BFS runs two frontiers to depth d/2, so expansions are
#   O(2 * b^(d/2)) = O(b^(d/2)) with similar space usage.
# - In worst-case graphs (V vertices, E edges), both are O(V + E); the benefit
#   is reduced search area when the frontiers meet well before exploring all V.

# Implement your graph + bidirectional search here
# Question: What is the time/space complexity of bidirectional search vs
# a single-source BFS, and when does it offer the biggest improvement?

from dataclasses import dataclass
from typing import Self, Any


@dataclass
class GraphNode:
    value: Any
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

    def _add(self, value: Any):
        if value in self._edges:
            return
        self._edges[value] = GraphNode(value, [])

    def validate_existance(self, node: str):
        if node not in self._edges:
            raise KeyError(f"{node=} does not exists")

    def _add_to_neighbor(self, me: Any, new_neighbor: Any):
        self.validate_existance(me)
        self.validate_existance(new_neighbor)

        # if exists, skip
        if any(e.value == new_neighbor for e in self._edges[me].neighbors):
            return
        self._edges[me].neighbors.append(self._edges[new_neighbor])

    def neighbors(self, node: Any):
        self.validate_existance(node)
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


def bidirectional_search(graph: Graph, start: Any, goal: Any) -> list[Any] | None:
    graph.validate_existance(start)
    graph.validate_existance(goal)
    if start == goal:
        return [start]

    q_s = Queue()
    q_g = Queue()
    q_s.enqueue(start)
    q_g.enqueue(goal)

    # visited + parent
    parent_s: dict[Any, Any | None] = {start: None}
    parent_g: dict[Any, Any | None] = {goal: None}

    # Track frontier sizes to expand level-by-level (since Queue has no len()).
    frontier_s = 1
    frontier_g = 1

    def expand_one_level(
        q: Queue,
        frontier_size: int,
        parent_me: dict[Any, Any | None],
        parent_other: dict[Any, Any | None],
    ) -> tuple[Any | None, int]:
        """
        Expand exactly one BFS level from q.
        Returns: (meeting_node or None, next_frontier_size)
        """
        next_frontier = 0

        for _ in range(frontier_size):
            cur = q.dequeue()

            for nb in graph.neighbors(cur):
                v = nb.value
                if v in parent_me:
                    continue

                parent_me[v] = cur
                if v in parent_other:
                    return v, 0  # meeting found; next frontier irrelevant

                q.enqueue(v)
                next_frontier += 1

        return None, next_frontier

    def build_path(meet: Any) -> list[Any]:
        # start -> meet
        left: list[Any] = []
        cur: Any | None = meet
        while cur is not None:
            left.append(cur)
            cur = parent_s[cur]
        left.reverse()

        # meet -> goal (skip meet to avoid duplication)
        right: list[Any] = []
        cur = parent_g[meet]
        while cur is not None:
            right.append(cur)
            cur = parent_g[cur]

        return left + right

    while (not q_s.is_empty()) and (not q_g.is_empty()):
        # A common optimization: expand the smaller frontier first.
        if frontier_s <= frontier_g:
            meet, next_size = expand_one_level(q_s, frontier_s, parent_s, parent_g)
            if meet is not None:
                return build_path(meet)
            frontier_s = next_size
        else:
            meet, next_size = expand_one_level(q_g, frontier_g, parent_g, parent_s)
            if meet is not None:
                return build_path(meet)
            frontier_g = next_size

        # If a side couldn't add anything new, it will become 0 and then
        # its queue will eventually empty; loop will end with None.

    return None
