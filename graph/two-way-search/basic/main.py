# Implement your graph + bidirectional search here
# Question: What is the time/space complexity of bidirectional search vs
# a single-source BFS, and when does it offer the biggest improvement?

class Graph:
    def add_edge(self, u, v):
        raise NotImplementedError

    def neighbors(self, node):
        raise NotImplementedError


def bidirectional_search(graph, start, goal):
    raise NotImplementedError
