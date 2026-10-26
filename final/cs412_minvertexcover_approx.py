"""
Minimum Vertex Cover - 2-Approximation Algorithm
Author: Colin Finnegan
Algorithm: Standard 2-approximation using maximal matching
Approximation Ratio: 2 (guaranteed)
Time Complexity: O(|V| + |E|)
"""

import time
import sys
from typing import Set, Tuple, List, Dict

def read_graph(filename: str) -> Tuple[Set[str], List[Tuple[str, str]]]:
    """Same as exact solution"""
    vertices = set()
    edges = []
    
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    m = int(lines[0].strip())
    
    for i in range(1, m + 1):
        line = lines[i].strip()
        if line:
            u, v = line.split()
            vertices.add(u)
            vertices.add(v)
            edges.append((u, v))
    
    return vertices, edges

def approximate_vertex_cover(vertices: Set[str], edges: List[Tuple[str, str]]) -> Set[str]:
    """
    2-approximation algorithm for vertex cover
    Based on maximal matching approach
    
    Steps:
    1. Find a maximal matching
    2. Add both endpoints of each matched edge
    
    Guarantee: |C| ≤ 2 * |OPT|
    """
    cover = set()
    matched = set()
    
    # Create adjacency list
    adj_list: Dict[str, List[str]] = {v: [] for v in vertices}
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Find maximal matching greedily
    for u, v in edges:
        if u not in matched and v not in matched:
            cover.add(u)
            cover.add(v)
            matched.add(u)
            matched.add(v)
    
    # For isolated vertices or special cases
    for edge in edges:
        u, v = edge
        if u not in cover and v not in cover:
            # If edge not covered, add one endpoint (this shouldn't happen)
            cover.add(u)
    
    return cover

def main():
    if len(sys.argv) != 2:
        print("Usage: python cs412_minvertexcover_approx.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Read graph
    vertices, edges = read_graph(input_file)
    
    # Start timer
    start_time = time.time()
    
    # Find approximate vertex cover
    cover = approximate_vertex_cover(vertices, edges)
    
    # End timer
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    # Output result
    print(" ".join(sorted(cover)))
    
    # Print debug info
    print(f"Time taken: {elapsed_time:.6f} seconds", file=sys.stderr)
    print(f"Graph size: {len(vertices)} vertices, {len(edges)} edges", file=sys.stderr)
    print(f"Cover size: {len(cover)} vertices", file=sys.stderr)
    print(f"Approximation ratio upper bound: 2", file=sys.stderr)

if __name__ == "__main__":
    main()