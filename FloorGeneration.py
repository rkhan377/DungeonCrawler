import numpy as np
import Constants
import matplotlib.pyplot as plt
from Floor import Floor
from Room import Room


floor = Floor(Constants.ROW,Constants.COL)
floor.generateRooms()
floor.fill()


plt.title([len(floor.rooms)])
floor = np.array(floor.arr)
plt.imshow(floor, interpolation='none')
plt.show()
