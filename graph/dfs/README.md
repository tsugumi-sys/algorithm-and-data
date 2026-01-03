Interface

    class Graph:
        add_edge(u, v): add an undirected edge between u and v (create nodes if needed)
        neighbors(node): return the iterable of neighbors for node in insertion order

    dfs(graph, start): return a list of nodes visited in depth-first pre-order starting from start

Traversal rules

- The graph is undirected; add_edge(u, v) connects both ways and ignores duplicate edges.
- Preserve insertion order when exploring neighbors so traversal order is deterministic.
- Raise KeyError if start is not in the graph.
