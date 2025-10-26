# benchmark.py
import csv
from graph_io import read_input, write_output
from algorithms import Graph, prim_mst, kruskal_mst, Tracker
import os

def run_all(input_path="input.json", out_json="output.json", out_csv="results.csv"):
    data = read_input(input_path)
    results = []
    os.makedirs("docs", exist_ok=True)
    csv_rows = []
    header = ["graph_id","vertices","edges",
              "algorithm","total_cost","execution_time_ms",
              "comparisons","unions","finds","heap_ops","other_ops"]
    for g in data.get("graphs", []):
        gid = g.get("id")
        nodes = g.get("nodes", [])
        edges = g.get("edges", [])
        graph = Graph(nodes, edges)
        # Prim
        t1 = Tracker()
        prim_res = prim_mst(graph, t1)
        # Kruskal
        t2 = Tracker()
        kruskal_res = kruskal_mst(graph, t2)

        result_entry = {
            "graph_id": gid,
            "input_stats": {"vertices": len(nodes), "edges": len(edges)},
            "prim": prim_res,
            "kruskal": kruskal_res
        }
        results.append(result_entry)

        # CSV rows
        for name,res,tracker in [("prim", prim_res, prim_res['operations_count']),
                                 ("kruskal", kruskal_res, kruskal_res['operations_count'])]:
            ops = res['operations_count']
            csv_rows.append([
                gid, len(nodes), len(edges),
                name,
                res['total_cost'],
                res['execution_time_ms'],
                ops.get('comparisons',0),
                ops.get('unions',0),
                ops.get('finds',0),
                ops.get('heap_ops',0),
                ops.get('other_ops',0)
            ])

    write_output(results, path=out_json)
    # write CSV
    with open(out_csv, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(csv_rows)
    print(f"Done. JSON -> {out_json}, CSV -> {out_csv}")

if __name__ == "__main__":
    run_all()
