import random

# represents one particle in the simulation. Every particle is initialised with the state "healthy"
class Particle:
    def __init__(self, x, y):
        #print("Particle created")
        self.x = x
        self.y = y
        self.state = "healthy"
        self.infectionCounter = 0   # this is for checking how many days a particle was sick later

    # function moves a particle in a random direction. Stepsize: 1
    def move(self):
        # only move when it is not dead
        if(self.state != "dead"):
            axis = random.randint(1, 2) # 1: x-Axis; 2: y-Axis
            direction = random.randint(1, 2) # 1: down/left 2: up/right
            if(axis == 1):
                if(direction == 1 and self.x > 0):
                    self.x = self.x - 1
                elif(self.x < 195):
                    self.x = self.x + 1
            else:
                if (direction == 1 and self.y > 0):
                    self.y = self.y - 1
                elif(self.y < 195):
                    self.y = self.y + 1