# tests/test_mst.py
import pytest
from algorithms import Graph, prim_mst, kruskal_mst

# small sample graph
def sample_graph():
    nodes = ["A","B","C","D","E"]
    edges = [
        {"from":"A","to":"B","weight":4},
        {"from":"A","to":"C","weight":3},
        {"from":"B","to":"C","weight":2},
        {"from":"B","to":"D","weight":5},
        {"from":"C","to":"D","weight":7},
        {"from":"C","to":"E","weight":8},
        {"from":"D","to":"E","weight":6}
    ]
    return Graph(nodes, edges)

def edges_cost(edges):
    return sum(e['weight'] for e in edges)

def test_prim_vs_kruskal_equal_cost():
    g = sample_graph()
    p = prim_mst(g)
    k = kruskal_mst(g)
    assert p['total_cost'] == k['total_cost']
    assert p['total_cost'] == 16  # expected from example

def test_mst_edge_count():
    g = sample_graph()
    p = prim_mst(g)
    k = kruskal_mst(g)
    n = len(g.nodes)
    assert len(p['mst_edges']) == n-1
    assert len(k['mst_edges']) == n-1

def test_mst_connects_all_nodes():
    g = sample_graph()
    p = prim_mst(g)
    nodes = set(g.nodes)
    p_nodes = set()
    for e in p['mst_edges']:
        p_nodes.add(e['from']); p_nodes.add(e['to'])
    assert nodes == p_nodes

def test_disconnected_graph():
    # graph with two components
    nodes = ["A","B","C","D"]
    edges = [
        {"from":"A","to":"B","weight":1},
        # component 2: C - D isolated component without edge to A/B
    ]
    g = Graph(nodes, edges)
    p = prim_mst(g)
    # Should not include all nodes in MST (Prim cannot connect components) -> edges < n-1
    assert len(p['mst_edges']) < len(nodes)-1
    # Kruskal also will produce less edges
    k = kruskal_mst(g)
    assert len(k['mst_edges']) < len(nodes)-1
