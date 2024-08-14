import numpy as np

def label_grid(grid):
    row,column = np.shape(grid)
    print(column)

    for i in range(row):
        for j in range(column):
            #Check if cell is already a mine, if not start labeling process
            if grid[i][j] != -1:
                adjacent_mines = 0

                if i==0 and j==0:
                    if grid[i][j+1] ==-1:
                        adjacent_mines += 1
                    if grid[i+1][j] ==-1:
                        adjacent_mines+= 1
                    if grid[i+1][j+1] ==-1:
                        adjacent_mines += 1

                elif i==0 and j==column-1:
                    if grid[i][j-1] ==-1:
                        adjacent_mines += 1
                    if grid[i+1][j] ==-1:
                        adjacent_mines+= 1
                    if grid[i+1][j-1] ==-1:
                        adjacent_mines += 1

                elif i== row-1 and j== 0:
                    if grid[i][j+1] ==-1:
                        adjacent_mines += 1
                    if grid[i-1][j] ==-1:
                        adjacent_mines+= 1
                    if grid[i-1][j+1] ==-1:
                        adjacent_mines += 1

                elif i== row-1 and j== column-1:
                    if grid[i][j-1] ==-1:
                        adjacent_mines += 1
                    if grid[i-1][j] ==-1:
                        adjacent_mines+= 1
                    if grid[i-1][j-1] ==-1:
                        adjacent_mines += 1

                elif i == 0 and j!= 0 and j!= column-1:
                    if grid[i][j - 1] == -1:
                        adjacent_mines += 1
                    if grid[i][j + 1] == -1:
                        adjacent_mines += 1
                    if grid[i + 1][j] == -1:
                        adjacent_mines += 1
                    if grid[i + 1][j + 1] == -1:
                        adjacent_mines += 1
                    if grid[i + 1][j - 1] == -1:
                        adjacent_mines += 1

                elif i == row-1 and j!= 0 and j!= column-1:
                    if grid[i][j - 1] == -1:
                        adjacent_mines += 1
                    if grid[i][j + 1] == -1:
                        adjacent_mines += 1
                    if grid[i - 1][j] == -1:
                        adjacent_mines += 1
                    if grid[i - 1][j + 1] == -1:
                        adjacent_mines += 1
                    if grid[i - 1][j - 1] == -1:
                        adjacent_mines += 1

                elif j == 0 and i!= 0 and i!= row-1:
                    if grid[i + 1][j] == -1:
                        adjacent_mines += 1
                    if grid[i - 1][j] == -1:
                        adjacent_mines += 1
                    if grid[i][j + 1] == -1:
                        adjacent_mines += 1
                    if grid[i + 1][j + 1] == -1:
                        adjacent_mines += 1
                    if grid[i - 1][j + 1] == -1:
                        adjacent_mines += 1

                elif j == column-1 and i!= 0 and i!= row-1:
                    if grid[i + 1][j] == -1:
                        adjacent_mines += 1
                    if grid[i - 1][j] == -1:
                        adjacent_mines += 1
                    if grid[i][j - 1] == -1:
                        adjacent_mines += 1
                    if grid[i + 1][j - 1] == -1:
                        adjacent_mines += 1
                    if grid[i - 1][j - 1] == -1:
                        adjacent_mines += 1

                else:
                    if grid[i + 1][j] == -1:
                        adjacent_mines += 1
                    if grid[i - 1][j] == -1:
                        adjacent_mines += 1
                    if grid[i][j - 1] == -1:
                        adjacent_mines += 1
                    if grid[i + 1][j - 1] == -1:
                        adjacent_mines += 1
                    if grid[i - 1][j - 1] == -1:
                        adjacent_mines += 1
                    if grid[i][j + 1] == -1:
                        adjacent_mines += 1
                    if grid[i + 1][j + 1] == -1:
                        adjacent_mines += 1
                    if grid[i - 1][j + 1] == -1:
                        adjacent_mines += 1
                grid[i][j] = adjacent_mines










    return grid