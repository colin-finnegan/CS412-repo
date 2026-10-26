# name: Colin Finnegan

def solve():
    # Read input
    sections = list(map(int, input().split()))
    target = int(input())
    n = len(sections)

    # DP table initialization
    INF = float("inf")
    dp = [[INF] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # base case

    # Fill DP table
    for i in range(1, n + 1):
        length = sections[i - 1]
        for t in range(target + 1):
            # skip current section type
            dp[i][t] = dp[i - 1][t]
            # use current section type if possible
            if t >= length and dp[i][t - length] + 1 < dp[i][t]:
                dp[i][t] = dp[i][t - length] + 1

    # Backtrack to find solution counts
    used = [0] * n
    i, t = n, target
    while t > 0 and i > 0:
        if dp[i][t] == dp[i - 1][t]:
            # this section not used
            i -= 1
        else:
            # this section used
            used[i - 1] += 1
            t -= sections[i - 1]

    # Output
    for i in range(n):
        print(f"{used[i]} of length {sections[i]}")
    print(f"{dp[n][target]} rocket sections minimum")


def main():
    solve()


if __name__ == "__main__":
    main()
