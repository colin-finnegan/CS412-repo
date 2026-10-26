"""
    name: Colin Finnegan

"""


def solve():
    # Read input
    sections = list(map(int, input().split()))
    target = int(input())

    n = len(sections)
    best_count = [float("inf")]
    best_combo = [[]]

    def backtrack(index, remaining, used, count):
        # index = current section we're considering
        if remaining == 0:
            if count < best_count[0]:
                best_count[0] = count
                best_combo[0] = used[:]
            return

        if index < 0:  # ran out of section types
            return

        length = sections[index]
        max_num = remaining // length

        for k in range(max_num, -1, -1):
            new_count = count + k
            if new_count >= best_count[0]:  # prune
                continue
            used[index] = k
            backtrack(index - 1, remaining - k * length, used, new_count)
            used[index] = 0  # reset

    backtrack(n - 1, target, [0] * n, 0)

    # Output
    for i in range(n):
        print(f"{best_combo[0][i]} of length {sections[i]}")
    print(f"{best_count[0]} rocket sections minimum")


def main():
    solve()


if __name__ == "__main__":
    main()
