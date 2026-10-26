""" Lab8 Railroads
Version: 2025
Author: Colin Finnegan
"""


import math
from connected_components import count_and_label


def distance(cord1, cord2):

    x_val = math.pow((cord2[0] - cord1[0]), 2)
    y_val = math.pow((cord2[1] - cord1[1]), 2)
    distance = math.sqrt(x_val + y_val)
    return distance


def build_graph(cords):
    graph = {i: {} for i in range(len(cords))}
    n = len(cords)
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(cords[i], cords[j])
            graph[i][j] = d
            graph[j][i] = d

    return graph


def boruvka(full_graph):
    n = len(full_graph)
    mst_graph = {i: {} for i in range(n)}
    mst_cost = 0.0
    mst_edges = []

    count, labels = count_and_label(mst_graph)

    while count > 1:
        cheapest = {}

        for u in full_graph:
            for v, w in full_graph[u].items():
                if labels[u] != labels[v]:
                    comp_u = labels[u]
                    comp_v = labels[v]
                    if comp_u not in cheapest or w < cheapest[comp_u][2]:
                        cheapest[comp_u] = (u, v, w)
                    if comp_v not in cheapest or w < cheapest[comp_v][2]:
                        cheapest[comp_v] = (u, v, w)

        added = set()
        for (u, v, w) in cheapest.values():
            edge = tuple(sorted((u, v)))
            if edge not in added and labels[u] != labels[v]:
                added.add(edge)
                mst_cost += w
                mst_edges.append((u, v, w))
                mst_graph[u][v] = w
                mst_graph[v][u] = w

        count, labels = count_and_label(mst_graph)

    return mst_cost, mst_edges


def main():

    n = int(input())
    cords = []
    for _ in range(n):
        x, y = map(float, input().split(" "))
        cords.append((x, y))

    graph = build_graph(cords)
    cost, edges = boruvka(graph)
    print(f"${cost:.1f}M")
    

if __name__ == "__main__":
    main()

