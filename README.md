# DAA3
# Assignment 3 – City Transportation Network Optimization

## Objective
To find the Minimum Spanning Tree (MST) using Prim’s and Kruskal’s algorithms for optimizing a city’s road network.

## Algorithms Implemented
- Prim’s Algorithm (Heap-based)
- Kruskal’s Algorithm (Union-Find)

## Input
Graph data stored in `input.json`.

## Output
Results stored in `output.json`, including:
- MST total cost
- Operation count
- Execution time

## Comparison Summary
| Graph ID | Prim Time (ms) | Kruskal Time (ms) | Total Cost |
|-----------|----------------|-------------------|-------------|
| 1         | 1.52           | 1.28              | 16          |
| 2         | 0.87           | 0.92              | 6           |

## Conclusion
- Both algorithms produce the same total MST cost.
- Prim’s algorithm is more efficient on dense graphs.
- Kruskal’s performs better on sparse graphs.
