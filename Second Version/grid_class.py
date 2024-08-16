import numpy as np
import random


class minesweeper:
    def __init__(self,grid_row,grid_column,number_of_mines):
        self.grid_row = grid_row
        self.grid_column = grid_column
        self.number_of_mines = number_of_mines
        self.internal_grid = self.generate_grid()


    def generate_grid(self):
        grid = np.zeros((self.grid_row, self.grid_column))

        # MINE PLACEMENT #
        ##################
        #Pick random numbers (# of mines) from 0 to (grid_row*grid_column -1)
        mine_placement = random.sample(np.arange(self.grid_row * self.grid_column).tolist(), self.number_of_mines)

        #Annotate place of mines within the grid
        for i in mine_placement:
            mine_row = i // self.grid_column
            mine_column = i % self.grid_column
            grid[mine_row][mine_column] = -1

        # GRID LABELING
        ##################
        #Find each mine within the grid and get coordinates of all neighbouring cells
        mine_adjacent_cells = []
        for i in range(self.grid_row):
            for j in range(self.grid_column):
                if grid[i][j] == -1:
                    mine_adjacent_cells.extend(
                        [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i + 1, j + 1), (i - 1, j - 1), (i + 1, j - 1),
                         (i - 1, j + 1)])

        #Check if the coordinate in the list is valid and not out of bounds.
        # --> If yes, add +1 in to that cell
        for coordinate in mine_adjacent_cells:
            if coordinate[0] <= self.grid_row - 1 and coordinate[1] <= self.grid_column - 1 and coordinate[0] >= 0 and \
                    coordinate[1] >= 0:
                if grid[coordinate[0]][coordinate[1]] != -1:
                    grid[coordinate[0]][coordinate[1]] += 1

        return grid



