import pytest

from main import Graph, bidirectional_search


def build_graph(edges):
    graph = Graph()
    for u, v in edges:
        graph.add_edge(u, v)
    return graph


def test_finds_shortest_path_in_undirected_graph():
    edges = [
        ("A", "B"),
        ("B", "C"),
        ("C", "D"),
        ("A", "E"),
        ("E", "D"),
    ]
    graph = build_graph(edges)
    path = bidirectional_search(graph, "A", "D")
    assert path in (["A", "E", "D"], ["D", "E", "A"])  # allow either direction as long as shortest
    assert len(path) == 3


def test_prefers_shortest_when_multiple_paths_exist():
    edges = [
        (1, 2),
        (2, 3),
        (3, 4),
        (1, 5),
        (5, 4),
        (2, 5),  # extra shorter option 1-2-5-4
    ]
    graph = build_graph(edges)
    path = bidirectional_search(graph, 1, 4)
    assert path in ([1, 2, 5, 4], [4, 5, 2, 1])
    assert len(path) == 4


def test_returns_none_when_no_path_exists():
    graph = build_graph([("A", "B"), ("C", "D")])
    assert bidirectional_search(graph, "A", "D") is None


def test_start_equals_goal_returns_singleton_path():
    graph = build_graph([("x", "y")])
    assert bidirectional_search(graph, "x", "x") == ["x"]


def test_raises_key_error_for_missing_nodes():
    graph = build_graph([("A", "B")])
    with pytest.raises(KeyError):
        bidirectional_search(graph, "A", "Z")
    with pytest.raises(KeyError):
        bidirectional_search(graph, "Z", "A")
