import numpy as np
import matplotlib.pyplot as plt

FLOOR = 0
WARP_BORDER = 1
BORDER = 2

ROW,COL = 56, 32
floor = [[0]*row for i in range(col)]


for i in range(col):
    for j in range(row):
        if i == 0 or j == 0 or i == 31 or j == 55:
            floor[i][j] = WARP_BORDER
        if (i == 1 or j == 1 or i == 30 or j == 54) and floor[i][j]==FLOOR:
            floor[i][j] = BORDER

floor = np.array(floor)
plt.imshow(floor, interpolation='none')
plt.grid()
plt.show()
