""" Greedy Algorithms Lab
Version: 2025
Author: Colin Finnegan
"""

import sys

def read_input():
    """
    Input format:
      Line 1: W  (nonnegative integer or float) - knapsack capacity
      Line 2: n  (nonnegative integer) - number of items
      Next n lines: each "name value weight"
    Returns: W (float), items list of dicts: {'name': str, 'value': float, 'weight': float}
    """
    data = sys.stdin.read().strip().split()
    if not data:
        return 0.0, []

    it = iter(data)
    try:
        W = float(next(it))
    except StopIteration:
        return 0.0, []

    try:
        n = int(next(it))
    except StopIteration:
        n = 0

    items = []
    for _ in range(n):
        try:
            name = next(it)
            value = float(next(it))
            weight = float(next(it))
        except StopIteration:
            break
        items.append({'name': name, 'value': value, 'weight': weight})

    return W, items

def fractional_knapsack(W, items):
    """
    Returns:
      - taken_items: list of tuples (name, value_taken, weight_taken)
        in order of decreasing value-per-weight ratio (ties preserved by stable sort).
      - total_value: float
    """
    processed = []
    for item in items:
        w = item['weight']
        v = item['value']
        if w == 0:
            ratio = float('inf') if v > 0 else 0.0
        else:
            ratio = v / w
        processed.append({
            'name': item['name'],
            'value': v,
            'weight': w,
            'ratio': ratio
        })

    # Sort by ratio descending
    processed.sort(key=lambda x: x['ratio'], reverse=True)

    capacity = float(W)
    taken = []
    total_value = 0.0

    for it in processed:
        if capacity <= 0:
            break

        if it['weight'] == 0:
            if it['value'] > 0:
                taken.append((it['name'], float(it['value']), 0.0))
                total_value += it['value']
            continue

        amount = min(it['weight'], capacity)
        value_taken = it['ratio'] * amount
        taken.append((it['name'], float(value_taken), float(amount)))
        total_value += value_taken
        capacity -= amount

    return taken, total_value

def main():
    W, items = read_input()
    taken, total_value = fractional_knapsack(W, items)

    # Print items line: each as name(value_two_decimals, weight_two_decimals)
    out_parts = []
    for name, val_taken, weight_taken in taken:
        out_parts.append(f"{name}({val_taken:.2f}, {weight_taken:.2f})")

    # Print exactly like sample: no trailing space at end of line
    if out_parts:
        print(" ".join(out_parts))
    else:
        print()

    # Print total value on second line (one decimal like sample)
    print(f"{total_value:.1f}")

if __name__ == "__main__":
    main()
