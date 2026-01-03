import pytest

from main import Graph, bfs


def build_sample_graph():
    graph = Graph()
    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "E"),
        ("E", "F"),
    ]
    for u, v in edges:
        graph.add_edge(u, v)
    return graph


def test_bfs_visits_level_by_level_in_insertion_order():
    graph = build_sample_graph()
    order = bfs(graph, "A")
    assert order == ["A", "B", "C", "D", "E", "F"]


def test_cycles_do_not_break_traversals():
    graph = build_sample_graph()
    # add a cycle C-D-B
    graph.add_edge("C", "D")
    order_bfs = bfs(graph, "A")

    assert order_bfs == ["A", "B", "C", "D", "E", "F"]


def test_starting_node_must_exist():
    graph = build_sample_graph()
    with pytest.raises(KeyError):
        bfs(graph, "Z")


def test_traversal_stays_in_connected_component():
    graph = build_sample_graph()
    graph.add_edge("X", "Y")  # disconnected component

    assert set(bfs(graph, "X")) == {"X", "Y"}
