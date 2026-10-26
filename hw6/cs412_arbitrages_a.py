""" HW6
Version: 2025
Author: Colin Finnegan
"""


import math


def main():
    n = int(input())
    graph = []
    currencies = set()
    rate_map = {}

    for i in range(n):
        cIn, cOut, xchange = input().split()
        rate = float(xchange)
        graph.append((cIn, cOut, -math.log(rate)))
        currencies.add(cIn)
        currencies.add(cOut)
        graph.append((cIn, cOut, -math.log(rate)))

        # Save the real rate for output later
        if cIn not in rate_map:
            rate_map[cIn] = {}
        rate_map[cIn][cOut] = rate

    # Run Bellman-Ford starting from any currency (graph may be disconnected)
    start_currency = next(iter(currencies))
    cycle = detect_arbitrage(graph, currencies, start_currency)

    if cycle is None:
        print("No Arbitrage Detected")
        return

    print("Arbitrage Detected")

    # Format: USD => EUR => JPY => TRY => USD
    cycle.append(cycle[0])  # bring back to starting point
    print(" => ".join(cycle))

    # Compute multiplicative factor
    product = 1.0
    for i in range(len(cycle)-1):
        a = cycle[i]
        b = cycle[i+1]
        product *= rate_map[a][b]

    print(f"{product:.5f} factor increase")


def detect_arbitrage(edges, vertices, start):
    dist = {v: float("inf") for v in vertices}
    parent = {v: None for v in vertices}
    dist[start] = 0

    # Relax edges |V| - 1 times
    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u

    # Check for negative cycle
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            # Found a negative cycle → arbitrage exists
            cycle_node = v

            # Move |V| steps to ensure the node is inside the cycle
            for _ in range(len(vertices)):
                cycle_node = parent[cycle_node]

            # Now reconstruct the cycle
            cycle = []
            cur = cycle_node
            while True:
                cycle.append(cur)
                cur = parent[cur]
                if cur == cycle_node:
                    break

            cycle.reverse()
            return cycle  # return list of vertex names in the arbitrage cycle

    return None


if __name__ == "__main__":
    main()