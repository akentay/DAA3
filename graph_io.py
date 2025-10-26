# graph_io.py
import json
from algorithms import Graph

def read_input( path="input.json"):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    # expect {"graphs": [ {id, nodes, edges}, ... ]}
    return data

def write_output(results, path="output.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"results": results}, f, indent=2, ensure_ascii=False)
