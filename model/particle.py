import random

class Particle:
    def __init__(self, x, y, radius):
        print("Particle created")
        self.x = x
        self.y = y
        self.radius = radius
        self.state = "healthy"
        self.infectionCounter = 0

    def move(self):
        if(self.state != "dead"):
            axis = random.randint(1, 2) # 1: x-Axis; 2: y-Axis
            direction = random.randint(1, 2) # 1: down/left 2: up/right
            if(axis == 1):
                if(direction == 1 and self.x > 0):
                    self.x = self.x - 1
                elif(self.x < 200):
                    self.x = self.x + 1
            else:
                if (direction == 1 and self.y > 0):
                    self.y = self.y - 1
                elif(self.y < 200):
                    self.y = self.y + 1