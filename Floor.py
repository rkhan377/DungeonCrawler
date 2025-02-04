import Constants
import math
import Room
import random
MAX_M = 4
MAX_N = 4
MIN_M = 2
MIN_N = 1

class Floor:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.arr = [[Constants.WALL]*row for i in range(col)]
        self.rooms = []

    def generateRooms(self):
        m = (random.randint(MIN_M,MAX_M))
        n = (random.randint(MIN_N,MAX_N))
        numSections = m*n
        print(numSections)
        sectionWidth =math.floor(Constants.ROW/m)
        sectionHeight = math.floor(Constants.COL/n)
        for i in range(m):
            for j in range(n):
                currSectionOriginX = (sectionWidth*i)
                currSectionOriginY = (sectionHeight*j)
                room = Room.Room(currSectionOriginX,currSectionOriginY,sectionWidth,sectionHeight)
                self.rooms.append(room)

    def isXInARoom(self, x):
        for room in self.rooms:
            if x <= room.secondX and room.firstX <= x:
                return room
        return None
    
    def isYInARoom(self, y):
        for room in self.rooms:
            if y <= room.secondY and room.firstY <= y:
                return room
        return None
    
    def fill(self):
        for i in range(self.col):
            for j in range(self.row):
                if i == 0 or j == 0 or i == 31 or j == 55:
                    self.arr[i][j] = Constants.WARP_BORDER
                elif (i == 1 or j == 1 or i == 30 or j == 54) and self.arr[i][j]==Constants.FLOOR:
                    self.arr[i][j] = Constants.BORDER
                elif (isXInARoom(i)!=None) and (isYInARoom(j)!=None):
                    self.arr[i][j]= Constants.FLOOR
