import Constants
import Room
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

    def borders(self):
        for i in range(self.col):
            for j in range(self.row):
                if i == 0 or j == 0 or i == 31 or j == 55:
                    self.arr[i][j] = Constants.WARP_BORDER
                if (i == 1 or j == 1 or i == 30 or j == 54) and self.arr[i][j]==Constants.FLOOR:
                    self.arr[i][j] = Constants.BORDER

    def generateRooms(self):
        m = (random.randint(MIN_M,MAX_M))
        n = (random.randint(MIN_N,MAX_N))
        numSections = m*n
        print(numSections)
        sectionWidth =Constants.ROW/m
        sectionHeight = Constants.COL/n
        for i in range(m):
            for j in range(i):
                room = Room(sectionWidth+(sectionWidth*i),sectionHeight+(sectionHeight*j))
                self.rooms.append(room)
    