import numpy as np

def label_grid(grid):
    row,column = np.shape(grid)

    mine_adjacent_cells = []

    for i in range(row):
        for j in range(column):
            if grid[i][j] == -1:
                mine_adjacent_cells.extend([(i+1,j),(i-1,j),(i,j+1),(i,j-1),(i+1,j+1),(i-1,j-1),(i+1,j-1),(i-1,j+1)])

    for coordinate in mine_adjacent_cells:
        if coordinate[0] <= row-1 and coordinate[1] <= column-1 and coordinate[0] >= 0 and coordinate[1] >= 0:
            if grid[coordinate[0]][coordinate[1]] != -1:
                grid[coordinate[0]][coordinate[1]] += 1

    return grid
