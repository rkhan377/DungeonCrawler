import FloorGeneration
import random
MAX_M = 9
MAX_N = 8
MIN_M = 2
MIN_N = 1

class Floor:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.arr = [[0]*row for i in range(col)]
        self.rooms = []

    def generateRooms():
        m = (random.randint(MIN_M,MAX_M))
        n = (random.randint(MIN_N,MAX_N))
        numSections = m*n
        print(numSections)
        sectionWidth =FloorGeneration.ROW/m
        sectionHeight = FloorGeneration.COL/n
    