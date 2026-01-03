# Implement your graph + bidirectional search here
# Complexity discussion:
# - Let b be branching factor and d be shortest-path distance.
# - Single-source BFS expands O(b^0 + ... + b^d) = O(b^d) nodes and space.
# - Bidirectional BFS runs two frontiers to depth d/2, so expansions are
#   O(2 * b^(d/2)) = O(b^(d/2)) with similar space usage.
# - In worst-case graphs (V vertices, E edges), both are O(V + E); the benefit
#   is reduced search area when the frontiers meet well before exploring all V.

class Graph:
    def add_edge(self, u, v):
        raise NotImplementedError

    def neighbors(self, node):
        raise NotImplementedError


def bidirectional_search(graph, start, goal):
    raise NotImplementedError
