from model.particle import Particle
# from model.particleState import ParticleState
# from model.statistics import Statistics
import random


class Simulation:
    def __init__(self, countParticles=100, radius=3):
        #print("Simulation Created")
        self.radius = radius
        self.stepCounter = 0
        self.particleList = {}
        # iterate through particleList and create as many particles as countParticles is. the positions are random
        for i in range(0, countParticles):
            rndmX = random.randint(0, 195)
            rndmY = random.randint(0, 195)
            self.particleList[i] = Particle(rndmX, rndmY)
        self.particleList[random.randint(0, len(self.particleList) - 1)].state = "infected" # set one particles state as "infected"

    def performStep(self):
        self.stepCounter += 1 # variable to know how many frames were already created
        #print("Simulation step {} processed.".format(self.stepCounter))
        # move every particle in particleList
        for i in range(0, len(self.particleList)):
            self.particleList[i].move()
        self.detectCollisions()

    # function searches for collisions with infected particles and overwrites particles state with a given possibility to "infected"
    def detectCollisions(self):
        for i in range(0, len(self.particleList)):
            for j in range(0, len(self.particleList)):
                if(abs(self.particleList[i].x -self.particleList[j].x) <= self.radius and abs(self.particleList[i].y - self.particleList[j].y) <= self.radius and self.particleList[i].state == "healthy" and self.particleList[j].state == "infected"): #and self.particleList[j].state == "infected"
                    infectionRate = 12 #Percent
                    rndm = random.randint(1, 100)
                    #print(rndm)
                    if(rndm <= infectionRate):
                        self.particleList[i].state = "infected"
    # sets the simulations radius
    def setRadius(self, radius):
        self.radius = radius
    # returns the current frame count
    def getData(self):
        return self.stepCounter
    # returns the particleList
    def getParticles(self):
        return self.particleList