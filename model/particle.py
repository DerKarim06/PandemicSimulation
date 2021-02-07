import random
import resources.strings as strings

# constants
MOVEMENT_RADIUS = 5
FRAMES_FOR_ONE_DAY = 60

class Particle:
    """this class represents one particle in the simulation. Every particle is initialised with the state HEALTHY"""
    def __init__(self, x, y, simulation, radius=3):
        self.simulation = simulation
        self.x = x
        self.y = y
        # initially calculate a Delta x and y for movement angle
        self.currentDeltaX = random.randint(-MOVEMENT_RADIUS, MOVEMENT_RADIUS)
        self.currentDeltaY = random.randint(-MOVEMENT_RADIUS, MOVEMENT_RADIUS)
        while(self.currentDeltaX == 0 and self.currentDeltaY == 0): # check whether the particle initially wants to stay at the same place
            self.currentDeltaY = random.randint(-MOVEMENT_RADIUS, MOVEMENT_RADIUS)
        self.stepX = self.currentDeltaX
        self.stepY = self.currentDeltaY
        self.state = strings.HEALTHY
        self.radius = radius
        self.infectionCounter = 0   # this is for checking how many days a particle was sick later
        self.is_colliding = False

    def calculate_delta_xy(self):
        """this function calculates a new delta x and y for the movement angle of the given particle"""
        self.currentDeltaX = random.randint(-MOVEMENT_RADIUS, MOVEMENT_RADIUS)
        self.stepX = self.currentDeltaX
        test = random.randint(-MOVEMENT_RADIUS, MOVEMENT_RADIUS)
        while (test == self.currentDeltaX):
            test = random.randint(-MOVEMENT_RADIUS, MOVEMENT_RADIUS)
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

    #
    def move(self):
        """this function moves a particle in a random direction. It uses the stepsize: 1"""
        if self.simulation.peopleStayAtHome:
            self.currentDeltaX = -1 * self.currentDeltaX
            self.currentDeltaY = -1 * self.currentDeltaY
        if self.is_colliding:
            self.calculate_delta_xy()
            self.is_colliding = False
        if (self.x == self.simulation.xBorder or self.x == 0 or self.y == self.simulation.yBorder or self.y == 0):
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
        """moves the particle 1 step in north direction"""
        if (self.y > 0):
            self.y -= 1
        self.stepY += 1

    def move_down(self):
        """moves the particle 1 step in south direction"""
        if (self.y < self.simulation.yBorder):
            self.y += 1
        self.stepY -= 1

    def move_left(self):
        """moves the particle 1 step in left direction"""
        if (self.x > 0):
            self.x -= 1
        self.stepX += 1

    def move_right(self):
        """moves the particle 1 step in right direction"""
        if (self.x < self.simulation.xBorder):
            self.x += 1
        self.stepX -= 1

    def incrementInfectionCounter(self):
        """this function increments the infectionCounter on the particle it is used on.
        IMPORTANT: it also uses side effects, as it is handling the recovery or death implicitly"""
        if self.state == strings.INFECTED:
            if self.infectionCounter < random.randint(self.simulation.minDaysInfected * FRAMES_FOR_ONE_DAY, self.simulation.maxDaysInfected * FRAMES_FOR_ONE_DAY):
                self.infectionCounter += 1
            else:
                if random.randint(0, 100) < self.simulation.deathRate:
                    self.state = strings.DEAD
                else:
                    self.infectionCounter = 0
                    self.state = strings.HEALTHY

    def detect_collisions(self, particle_list, infection_rate, infectionRadius):
        """this function detects collisions between the particle it is used on and all of the particles in the given list.
        Args:
            particle_list: A list of particles to check collisions on
            infection_rate: The rate of being infected while a collision occurs
            infectionRadius: The radius in which collisions should be handled
        """

        for j in range(0, len(particle_list)):
            if abs(self.x - particle_list[j].x) <= self.radius and abs(self.y - particle_list[j].y) <= self.radius and self != particle_list[j] and self.state != strings.DEAD and particle_list[j].state != strings.DEAD:
                self.is_colliding = True
                particle_list[j].is_colliding = True
            if abs(self.x - particle_list[j].x) <= infectionRadius and abs(self.y - particle_list[j].y) <= infectionRadius and self != particle_list[j] and ((self.state == strings.HEALTHY and particle_list[j].state == strings.INFECTED) or (self.state == strings.INFECTED and particle_list[j].state == strings.HEALTHY)):  # and particleList[j].state == "infected"
                rndm = random.randint(1, 100)
                if (rndm <= infection_rate):
                    if self.state == strings.HEALTHY:
                        self.state = strings.INFECTED
                    else:
                        particle_list[j].state = strings.INFECTED

    def setParticleRadius(self, radius):
        """sets particles radius

        Args:
            radius: the radius that should be set"""
        self.radius = radius