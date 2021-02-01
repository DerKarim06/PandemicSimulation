import random

# represents one particle in the simulation. Every particle is initialised with the state "healthy"
class Particle:
    def __init__(self, x, y, simulation, radius=3):
        self.simulation = simulation
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
        self.radius = radius
        self.infectionCounter = 0   # this is for checking how many days a particle was sick later
        self.is_colliding = False

    # function moves a particle in a random direction. Stepsize: 1

    def calculate_delta_xy(self):
        self.currentDeltaX = random.randint(-5, 5)
        self.stepX = self.currentDeltaX
        test = random.randint(-5, 5)
        while (test == self.currentDeltaX):
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

    def move(self):
        if self.is_colliding:
            self.calculate_delta_xy()
            self.is_colliding = False
        if (self.x == 195 or self.x == 0 or self.y == 195 or self.y == 0):
            self.calculate_delta_xy()
        if(self.stepX == 0 and self.stepY == 0):
            self.stepX = self.currentDeltaX
            self.stepY = self.currentDeltaY
        if(self.stepX != 0):
            if(self.stepX > 0):
                self.move_right()
            else:
                self.move_left()
        else:
            if(self.stepY > 0):
                self.move_down()
            else:
                self.move_up()

    def move_up(self):
        if (self.y > 0):
            self.y -= 1
        self.stepY += 1

    def move_down(self):
        if (self.y < 195):
            self.y += 1
        self.stepY -= 1

    def move_left(self):
        if (self.x > 0):
            self.x -= 1
        self.stepX += 1

    def move_right(self):
        if (self.x < 195):
            self.x += 1
        self.stepX -= 1

    def incrementInfectionCounter(self):
        if self.state == 'infected':
            if self.infectionCounter < random.randint(600, 1200):
                self.infectionCounter += 1
            else:
                if random.randint(0, 100) < self.simulation.deathRate:
                    self.state = 'dead'
                else:
                    self.infectionCounter = 0
                    self.state = 'healthy'

    def detect_collisions(self, particle_list, infection_rate, infectionRadius):
        for j in range(0, len(particle_list)):
            if abs(self.x - particle_list[j].x) <= self.radius and abs(self.y - particle_list[j].y) <= self.radius and self != particle_list[j] and self.state != "dead" and particle_list[j].state != "dead":
                self.is_colliding = True
                particle_list[j].is_colliding = True
            if abs(self.x - particle_list[j].x) <= infectionRadius and abs(self.y - particle_list[j].y) <= infectionRadius and self != particle_list[j] and ((self.state == "healthy" and particle_list[j].state == "infected") or (self.state == "infected" and particle_list[j].state == "healthy")):  # and particleList[j].state == "infected"
                rndm = random.randint(1, 100)
                if (rndm <= infection_rate):
                    if self.state == "healthy":
                        self.state = "infected"
                    else:
                        particle_list[j].state = "infected"

    # def move2(self):
    #     # only move when it is not dead
    #     if(self.state != "dead"):
    #         axis = random.randint(1, 2) # 1: x-Axis; 2: y-Axis
    #         direction = random.randint(1, 2) # 1: down/left 2: up/right
    #         if(axis == 1):
    #             if(direction == 1 and self.x > 0):
    #                 self.x = self.x - 1
    #             elif(self.x < 195):
    #                 self.x = self.x + 1
    #         else:
    #             if (direction == 1 and self.y > 0):
    #                 self.y = self.y - 1
    #             elif(self.y < 195):
    #                 self.y = self.y + 1