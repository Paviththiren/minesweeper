import numpy as np
import random
from grid_generator import generate_grid
from grid_labeling import label_grid
grid = generate_grid(5,5,1)
grid = label_grid(grid)
print(grid)



