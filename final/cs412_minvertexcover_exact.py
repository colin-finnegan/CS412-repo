"""
Minimum Vertex Cover - Exact Solution using Branch and Bound
Author: Colin Finnegan
Sources:
1. Introduction to Algorithms by Cormen et al. - Chapter 35 (Approximation Algorithms)
2. Algorithm Design Manual by Skiena - Vertex Cover problem
3. Python itertools documentation: https://docs.python.org/3/library/itertools.html
"""

import itertools
import time
import sys
from typing import Set, Tuple, List

def read_graph(filename: str) -> Tuple[Set[str], List[Tuple[str, str]]]:
    """
    Read graph from file format:
    First line: number of edges m
    Following m lines: vertices u v
    
    Returns:
        vertices: set of all vertices
        edges: list of edges as tuples (u, v)
    """
    vertices = set()
    edges = []
    
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    # First line is number of edges
    m = int(lines[0].strip())
    
    for i in range(1, m + 1):
        line = lines[i].strip()
        if line:
            u, v = line.split()
            vertices.add(u)
            vertices.add(v)
            edges.append((u, v))
    
    return vertices, edges

def is_vertex_cover(vertices: Set[str], edges: List[Tuple[str, str]], candidate: Set[str]) -> bool:
    """
    Check if the candidate set covers all edges.
    An edge is covered if at least one of its endpoints is in candidate.
    """
    for u, v in edges:
        if u not in candidate and v not in candidate:
            return False
    return True

def exact_vertex_cover(vertices: Set[str], edges: List[Tuple[str, str]]) -> Set[str]:
    """
    Exact solution using branch and bound approach.
    Tries all possible subsets in increasing size order.
    
    Time Complexity: O(2^n * m) where n = |V|, m = |E|
    """
    vertices_list = list(vertices)
    
    # Try all possible sizes from 1 to n
    for k in range(1, len(vertices_list) + 1):
        # Generate all combinations of size k
        for combo in itertools.combinations(vertices_list, k):
            candidate = set(combo)
            if is_vertex_cover(vertices, edges, candidate):
                return candidate
    
    # Should never reach here for a connected graph
    return set()

def main():
    if len(sys.argv) != 2:
        print("Usage: python cs412_minvertexcover_exact.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Read the graph
    vertices, edges = read_graph(input_file)
    
    # Start timer
    start_time = time.time()
    
    # Find exact vertex cover
    cover = exact_vertex_cover(vertices, edges)
    
    # End timer
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    # Output result
    print(" ".join(sorted(cover)))
    
    # Print debug info to stderr
    print(f"Time taken: {elapsed_time:.6f} seconds", file=sys.stderr)
    print(f"Graph size: {len(vertices)} vertices, {len(edges)} edges", file=sys.stderr)
    print(f"Cover size: {len(cover)} vertices", file=sys.stderr)

if __name__ == "__main__":
    main()