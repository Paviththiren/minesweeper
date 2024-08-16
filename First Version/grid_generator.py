import numpy as np
import random
def generate_grid(grid_row,grid_column,number_of_mines):
    grid = np.zeros((grid_row, grid_column))
    mine_placement = random.sample(np.arange(grid_row*grid_column).tolist(), number_of_mines)
    for i in mine_placement:
        mine_row = i // grid_column
        mine_column = i % grid_column
        grid[mine_row][mine_column] = -1

    return grid



