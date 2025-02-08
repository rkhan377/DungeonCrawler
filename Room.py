import random

class Room:

#rename variables later to be more readable
    def __init__(self, xS,yS, widthS, heightS):
        self.firstX= random.randint(xS, xS+widthS-1)
        self.firstY = random.randint(yS, yS+heightS-1)
        
        self.secondX= random.randint(self.firstX+1, xS+widthS)
        self.secondY = random.randint(self.firstY+1, yS+heightS)

        self.width = self.secondX - self.firstX
        self.height = self.secondY - self.firstY
        