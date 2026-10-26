"""
    name: Colin Finnegan

"""

def main():
    n = int(input())
    missing_i, missing_j = map(int, input().split())
    
    size = 2 ** n
    grid = [[-1] * size for _ in range(size)]
    grid[missing_i][missing_j] = -1
    
    tile_counter = [0]
    
    def tile_grid(top, left, size, missing_i, missing_j):
        if size == 1:
            return
        
        half = size // 2
        quadrant = 0
        
        if missing_i < top + half and missing_j < left + half:
            quadrant = 0
        elif missing_i < top + half and missing_j >= left + half:
            quadrant = 1
        elif missing_i >= top + half and missing_j < left + half:
            quadrant = 2
        else:
            quadrant = 3

        if quadrant != 0:
            if grid[top + half - 1][left + half - 1] == -1:
                grid[top + half - 1][left + half - 1] = tile_counter[0]
        if quadrant != 1:
            if grid[top + half - 1][left + half] == -1:
                grid[top + half - 1][left + half] = tile_counter[0]
        if quadrant != 2:
            if grid[top + half][left + half - 1] == -1:
                grid[top + half][left + half - 1] = tile_counter[0]
        if quadrant != 3:
            if grid[top + half][left + half] == -1:
                grid[top + half][left + half] = tile_counter[0]
        
        tile_counter[0] += 1
        
        if quadrant == 0:
            tile_grid(top, left, half, missing_i, missing_j)
            tile_grid(top, left + half, half, top + half - 1, left + half)
            tile_grid(top + half, left, half, top + half, left + half - 1)
            tile_grid(top + half, left + half, half, top + half, left + half)
        elif quadrant == 1:
            tile_grid(top, left, half, top + half - 1, left + half - 1)
            tile_grid(top, left + half, half, missing_i, missing_j)
            tile_grid(top + half, left, half, top + half, left + half - 1)
            tile_grid(top + half, left + half, half, top + half, left + half)
        elif quadrant == 2:
            tile_grid(top, left, half, top + half - 1, left + half - 1)
            tile_grid(top, left + half, half, top + half - 1, left + half)
            tile_grid(top + half, left, half, missing_i, missing_j)
            tile_grid(top + half, left + half, half, top + half, left + half)
        else:
            tile_grid(top, left, half, top + half - 1, left + half - 1)
            tile_grid(top, left + half, half, top + half - 1, left + half)
            tile_grid(top + half, left, half, top + half, left + half - 1)
            tile_grid(top + half, left + half, half, missing_i, missing_j)
    
    tile_grid(0, 0, size, missing_i, missing_j)
    
    for i in range(size):
        row = []
        for j in range(size):
            if grid[i][j] == -1:
                row.append("-1")
            else:
                row.append(f"{grid[i][j]:02d}")
        print(" ".join(row))


if __name__ == "__main__":
    main()