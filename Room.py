class Room:
    def __init__(self, row, col):
        self.x = 0
        self.y = 0
        self.row = row
        self.col = col
    
    def setRelativePosition(self, floor):
        self.x = floor.row - self.row
        self.y = floor.col - self.col

    #def generateItems, generateEnemies