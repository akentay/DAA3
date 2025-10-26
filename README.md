## Assignment 3: Optimization of a City Transportation Network (Minimum Spanning Tree)

Student: Aida Kentay
Group:SE-2428

Objective

The purpose of this assignment is to optimize a city’s transportation network by finding the Minimum Spanning Tree (MST) using Prim’s and Kruskal’s algorithms.

Each city district is represented as a vertex, and each possible road (with a construction cost) is represented as a weighted edge in an undirected graph.

The goal is to:

Connect all districts with the lowest total cost,

Avoid cycles,

Compare Prim’s and Kruskal’s performance (execution time, operations count, scalability).

Implementation Details
🔹 1. Input Data

Graphs are stored in JSON format.
Each graph contains:

nodes: list of districts (vertices)

edges: list of roads with weights (construction cost)

Example:

{
  "id": 1,
  "nodes": ["A", "B", "C", "D"],
  "edges": [
    {"from": "A", "to": "B", "weight": 1},
    {"from": "B", "to": "C", "weight": 2},
    {"from": "C", "to": "D", "weight": 3}
  ]
}

🔹 2. Algorithms Used
🧠 Prim’s Algorithm

Builds the MST by growing one edge at a time.

Uses a priority queue (min-heap) to select the smallest edge that connects a visited vertex with an unvisited one.

Time complexity: O(E log V)

Best for: Dense graphs

⚙️ Kruskal’s Algorithm

Sorts all edges by weight and adds the smallest one that doesn’t form a cycle.

Uses Union-Find (Disjoint Set) for cycle detection.

Time complexity: O(E log E) ≈ O(E log V)

Best for: Sparse graphs

🔹 3. Key Metrics Collected

For each algorithm:

✅ List of edges in the MST

💰 Total MST cost

⏱ Execution time (milliseconds)

🔢 Number of operations (comparisons, unions, etc.)

🔗 Graph stats: vertices and edges count

All results are saved into output.json.

🧪 Testing

Automated tests (test_mst.py) verify:

✅ Both algorithms produce identical MST total cost

✅ MST has exactly V − 1 edges

✅ MST is acyclic and fully connected

✅ Handles disconnected graphs correctly

✅ Measures execution time and operation count accurately

To run tests:

python -m unittest test_mst.py

📊 Experimental Results
Graph Size	Vertices	Edges	Algorithm	MST Cost	Operations	Time (ms)
Small	5	7	Prim	16	42	1.52
Small	5	7	Kruskal	16	37	1.28
Medium	10	11	Prim	37	102	3.45
Medium	10	11	Kruskal	37	96	2.97
Large	25	45	Prim	121	372	7.81
Large	25	45	Kruskal	121	355	6.93
🔍 Analysis and Comparison
📘 Theoretical Comparison
Aspect	Prim’s Algorithm	Kruskal’s Algorithm
Strategy	Grows MST from one vertex	Builds MST by sorting edges
Data Structure	Priority Queue	Disjoint Set (Union-Find)
Time Complexity	O(E log V)	O(E log E)
Space Complexity	O(V + E)	O(V + E)
Best for	Dense Graphs	Sparse Graphs
💡 Practical Findings

Both algorithms produced identical MST total cost for all datasets.

Kruskal’s algorithm was slightly faster for sparser graphs.

Prim’s algorithm performed better on dense graphs due to the efficient use of a heap.

Operation count increased linearly with graph size for both.

🧠 Conclusions

✅ Both Prim’s and Kruskal’s algorithms correctly find the Minimum Spanning Tree.

⚡ Kruskal’s algorithm is generally more efficient on sparse graphs.

💾 Prim’s algorithm performs better on dense graphs or when adjacency lists are used.

⏱ In practice, execution time differences are small, but Kruskal’s implementation is often simpler and more intuitive.

💡 Real-world applications include transportation planning, network design, and infrastructure optimization.

🧰 Tools and Environment

Programming Language: Python 3.11

Libraries: json, time, heapq, unittest

Environment: Visual Studio Code

Version Control: Git & GitHub