""" HW5 - Basic Graphs
Version: 2025
Author: Colin Finnegan
"""


def island_search(grid, row, col):
    if row >= len(grid) or row < 0:
        return 0
    
    if col >= len(grid[0]) or col < 0:
        return 0
    
    if grid[row][col] == 0:
        return 0

    if grid[row][col] == 1:
        grid[row][col] = 0
        return (1 + island_search(grid, row - 1, col)
                + island_search(grid, row + 1, col)
                + island_search(grid, row, col + 1)
                + island_search(grid, row, col - 1))
    

def main():
    max_island = 0
    grid = []
    n = int(input())
    for i in range(n):
        i = input().split(" ")
        i = [int(x) for x in i]
        grid.append(i)
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                current_size = island_search(grid, i, j)
                if current_size > max_island:
                    max_island = current_size
    
    print(max_island)


if __name__ == "__main__":
    main()
