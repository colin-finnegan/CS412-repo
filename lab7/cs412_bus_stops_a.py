""" Graph Search Lab
Version: 2025
Author: Colin Finnegan
"""

from collections import deque

def build_graph(n, segments):
    graph = {}
    for u, v in segments:
        if u not in graph:
            graph[u] = set()
        if v not in graph:
            graph[v] = set()
        graph[u].add(v)
        graph[v].add(u)  # bidirectional
    return graph

def bfs_path(graph, start, end):
    if start not in graph or end not in graph:
        return None
    
    queue = deque([start])
    visited = set([start])
    parent = {start: None}
    
    while queue:
        node = queue.popleft()
        if node == end:
            # reconstruct path
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]  # reverse
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)
    return None

def main():
    import sys
    data = sys.stdin.read().strip().splitlines()
    
    n = int(data[0])
    segments = [line.split() for line in data[1:n+1]]
    start, end = data[n+1].split()
    
    graph = build_graph(n, segments)
    path = bfs_path(graph, start, end)
    
    if path:
        print(" ".join(path))
    else:
        print("no route possible")

if __name__ == "__main__":
    main()
