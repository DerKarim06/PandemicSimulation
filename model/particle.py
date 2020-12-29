import random

# represents one particle in the simulation. Every particle is initialised with the state "healthy"
class Particle:
    def __init__(self, x, y):
        #print("Particle created")
        self.x = x
        self.y = y
        self.currentDeltaX = random.randint(-5, 5)
        self.currentDeltaY = random.randint(-5, 5)
        while(self.currentDeltaX == 0 and self.currentDeltaY == 0):
            self.currentDeltaY = random.randint(-5, 5)
        self.stepX = self.currentDeltaX
        self.stepY = self.currentDeltaY
        self.state = "healthy"
        self.infectionCounter = 0   # this is for checking how many days a particle was sick later

    # function moves a particle in a random direction. Stepsize: 1

    def move(self):
        if (self.x == 195 or self.x == 0 or self.y == 195 or self.y == 0):
                self.currentDeltaX = random.randint(-5, 5)
                self.stepX = self.currentDeltaX
                test = random.randint(-5, 5)
                while(test == self.currentDeltaX):
                    test = random.randint(-5, 5)
                self.currentDeltaY = test
                self.stepY = self.currentDeltaY
                if self.x == 0:
                    self.x += 1
                if self.x == 195:
                    self.x -= 1
                if self.y == 0:
                    self.y += 1
                if self.y == 195:
                    self.y -= 1
        if(self.stepX == 0 and self.stepY == 0):
            self.stepX = self.currentDeltaX
            self.stepY = self.currentDeltaY
        if(self.stepX != 0):
            if(self.stepX > 0):
                if(self.x < 195):
                    self.x += 1
                self.stepX -= 1
            else:
                if(self.x > 0):
                    self.x -= 1
                self.stepX += 1
        else:
            if(self.stepY > 0):
                if(self.y < 195):
                    self.y += 1
                self.stepY -= 1
            else:
                if(self.y > 0):
                    self.y -= 1
                self.stepY += 1

    def incrementInfectionCounter(self):
        if self.state == 'infected':
            if self.infectionCounter < random.randint(600, 1200):
                self.infectionCounter += 1
            else:
                if random.randint(0, 100) < 8:
                    self.state = 'dead'
                else:
                    self.infectionCounter = 0
                    self.state = 'healthy'

    def move2(self):
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