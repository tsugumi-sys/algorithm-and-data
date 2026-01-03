Interface

    class Graph:
        add_edge(u, v): add an undirected edge between u and v (create nodes if needed)
        neighbors(node): return the iterable of neighbors for node in insertion order

    bidirectional_search(graph, start, goal): return the shortest path as a list of nodes from start to goal (inclusive)

Behavior

- The graph is undirected; add_edge(u, v) connects both ways and ignores duplicate edges.
- Preserve insertion order when exploring neighbors so traversal order is deterministic.
- Raise KeyError if either start or goal is not in the graph.
- If no path exists, return None.
- If start == goal, return [start].
