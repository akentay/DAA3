# algorithms.py
import heapq
import time
from collections import defaultdict

class Tracker:
    def __init__(self):
        self.comparisons = 0
        self.unions = 0
        self.finds = 0
        self.heap_ops = 0
        

    def to_dict(self):
        return {
            "comparisons": self.comparisons,
            "unions": self.unions,
            "finds": self.finds,
            "heap_ops": self.heap_ops,
            "other_ops": self.other_ops
        }

class Graph:
    def __init__(self, nodes, edges):
        # nodes: list of labels
        # edges: list of dicts {'from': u, 'to': v, 'weight': w}
        self.nodes = list(nodes)
        self.edges = [dict(e) for e in edges]

    def adjacency(self):
        adj = defaultdict(list)
        for e in self.edges:
            u, v, w = e['from'], e['to'], e['weight']
            adj[u].append( (v, w) )
            adj[v].append( (u, w) )
        return adj

def prim_mst(graph: Graph, tracker: Tracker = None):
    if tracker is None:
        tracker = Tracker()
    start = time.time()
    nodes = graph.nodes
    if len(nodes) == 0:
        return {"mst_edges": [], "total_cost": 0, "operations_count": tracker.to_dict(), "execution_time_ms": 0.0}

    adj = graph.adjacency()
    visited = set()
    mst_edges = []
    total_cost = 0

    # choose start node deterministically (first in list)
    start_node = nodes[0]

    heap = []
    # push (weight, from, to)
    # push neighbors of start
    visited.add(start_node)
    for (v,w) in adj[start_node]:
        heapq.heappush(heap, (w, start_node, v))
        tracker.heap_ops += 1

    while heap and len(visited) < len(nodes):
        w,u,v = heapq.heappop(heap)  # minimal edge crossing cut
        tracker.heap_ops += 1
        tracker.comparisons += 1
        if v in visited:
            continue
        # accept edge
        visited.add(v)
        mst_edges.append({"from": u, "to": v, "weight": w})
        total_cost += w
        # push neighbors
        for (nx, nw) in adj[v]:
            if nx not in visited:
                heapq.heappush(heap, (nw, v, nx))
                tracker.heap_ops += 1

    end = time.time()
    return {
        "mst_edges": mst_edges,
        "total_cost": total_cost,
        "operations_count": tracker.to_dict(),
        "execution_time_ms": round((end - start) * 1000, 4)
    }

# ---------------- Kruskal -----------------
class UnionFind:
    def __init__(self, nodes, tracker: Tracker = None):
        self.parent = {n: n for n in nodes}
        self.rank = {n:0 for n in nodes}
        self.tracker = tracker

    def find(self, x):
        if self.tracker:
            self.tracker.finds += 1
        # path compression
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        if self.tracker:
            self.tracker.unions += 1
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False
        # union by rank
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True

def kruskal_mst(graph: Graph, tracker: Tracker = None):
    if tracker is None:
        tracker = Tracker()
    start = time.time()
    nodes = graph.nodes
    edges = list(graph.edges)
    # sort edges by weight
    # count comparisons as number of comparisons when sorting? We'll approximate: n*log n comparisons not counted precisely.
    edges_sorted = sorted(edges, key=lambda e: e['weight'])
    tracker.other_ops += len(edges_sorted)  # crude
    uf = UnionFind(nodes, tracker)
    mst_edges = []
    total_cost = 0
    for e in edges_sorted:
        u, v, w = e['from'], e['to'], e['weight']
        ru = uf.find(u)
        rv = uf.find(v)
        tracker.comparisons += 1
        if ru != rv:
            merged = uf.union(u, v)
            if merged:
                mst_edges.append({"from": u, "to": v, "weight": w})
                total_cost += w
        # stop early if MST complete
        if len(mst_edges) == len(nodes) - 1:
            break
    end = time.time()
    return {
        "mst_edges": mst_edges,
        "total_cost": total_cost,
        "operations_count": tracker.to_dict(),
        "execution_time_ms": round((end - start) * 1000, 4)
    }
