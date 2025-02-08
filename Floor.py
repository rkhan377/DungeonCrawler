import Constants
import math
import Room
import random
import matplotlib.pyplot as plt
MAX_M = 4
MAX_N = 4
MIN_M = 2
MIN_N = 1

class Floor:
    m = 0
    n = 0
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.arr = [[Constants.WALL]*row for i in range(col)]
        self.rooms = []
        self.border_lines = []

    def generateRooms(self):
        m = (random.randint(MIN_M,MAX_M))
        n = (random.randint(MIN_N,MAX_N))
        numSections = m*n
        print(numSections)
        sectionWidth =math.floor(Constants.COL/m)
        sectionHeight = math.floor(Constants.ROW/n)
        for i in range(m):
            for j in range(n):
                currSectionOriginX = (sectionWidth*i)
                currSectionOriginY = (sectionHeight*j)
                room = Room.Room(currSectionOriginX,currSectionOriginY,sectionWidth-1,sectionHeight-1)
                self.rooms.append(room)
                # Top and bottom horizontal lines (y = constant, x ranges from left to right)
                for x in range(currSectionOriginX, currSectionOriginX + sectionWidth):
                    self.border_lines.append((x, currSectionOriginY))  # Top border
                    self.border_lines.append((x, currSectionOriginY + sectionHeight - 1))  # Bottom border
                
                # Left and right vertical lines (x = constant, y ranges from top to bottom)
                for y in range(currSectionOriginY, currSectionOriginY + sectionHeight):
                    self.border_lines.append((currSectionOriginX, y))  # Left border
                    self.border_lines.append((currSectionOriginX + sectionWidth - 1, y))  # Right border


    def isXInARoom(self, x):
        for room in self.rooms:
            if x >= room.firstX and x <= room.secondX:
                return room
        return None
    
    def isYInARoom(self, y):
        for room in self.rooms:
            if y <= room.secondY and y >=room.firstY:
                return room
        return None
    
    def fill(self):
        for i in range(self.col):
            for j in range(self.row):
                if i == 0 or j == 0 or i == 31 or j == 55:
                    self.arr[i][j] = Constants.WARP_BORDER
                elif (i == 1 or j == 1 or i == 30 or j == 54) and self.arr[i][j]!=Constants.FLOOR:
                    self.arr[i][j] = Constants.BORDER
                elif (self.isXInARoom(i)!=None) and (self.isYInARoom(j)!=None):
                    self.arr[i][j]= Constants.FLOOR
                if ((i,j) in self.border_lines):
                    self.arr[i][j]= 400
                    
