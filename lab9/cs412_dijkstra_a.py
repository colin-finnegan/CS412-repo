""" Shortest Path Lab
Version: 2025
Author: Colin Finnegan
"""

from queue import PriorityQueue
import sys

def dijkstra(n, graph, start):
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n

    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        d, u = pq.get()
        if visited[u]:
            continue
        visited[u] = True

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pq.put((dist[v], v))

    return dist

def main():
    data = sys.stdin.read().strip().split()
    n, m, q = map(int, data[:3])
    index = 3

    # build adjacency list
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, data[index:index+3])
        graph[u].append((v, w))
        index += 3

    # process queries
    for _ in range(q):
        s, t = map(int, data[index:index+2])
        index += 2
        dist = dijkstra(n, graph, s)
        if dist[t] == float('inf'):
            print("Impossible")
        else:
            print(dist[t])

if __name__ == "__main__":
    main()
