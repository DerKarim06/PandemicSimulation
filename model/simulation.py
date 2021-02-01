import numpy as np

from model.particle import Particle
# from model.particleState import ParticleState
# from model.statistics import Statistics
import random


class Simulation:
    def __init__(self, countParticles=100, infectionRate=12, radius=5, initiallyInfected=1, deathRate=8):
        #print("Simulation Created")
        self.radius = radius
        self.infectionRate = infectionRate
        self.deathRate = deathRate
        self.stepCounter = 0
        self.particleList = []
        # iterate through particleList and create as many particles as countParticles is. the positions are random
        for i in range(0, countParticles):
            rndmX = random.randint(0, 195)
            rndmY = random.randint(0, 195)
            self.particleList.append(Particle(rndmX, rndmY, self))
        for i in range(initiallyInfected):
            self.particleList[i].state = "infected" # initially set particles state as "infected"

        self.dataX = [0]
        self.dataInfected = [initiallyInfected]
        self.dataHealthy = [countParticles - initiallyInfected]
        self.dataDead = [0]

    def performStep(self):
        self.stepCounter += 1 # variable to know how many frames were already created
        #print("Simulation step {} processed.".format(self.stepCounter))
        # move every particle in particleList
        j = 0
        k = 0
        l = 0
        for i in range(0, len(self.particleList)):
            self.particleList[i].detect_collisions(self.particleList[i:], self.infectionRate, self.radius)
        for i in range(0, len(self.particleList)):
            if(self.particleList[i].state != 'dead'):
                self.particleList[i].move()
            if self.particleList[i].state == 'infected':
                self.particleList[i].incrementInfectionCounter()
            if (self.stepCounter % 60 == 0): #Find variables for the statistic/csv
                if (self.particleList[i].state == 'dead'):
                    l += 1
                if (self.particleList[i].state == "infected"):
                    j += 1
                if (self.particleList[i].state == "healthy"):
                    k += 1
        if (self.stepCounter % 60 == 0): #add the variables to the lists
            self.dataX.append(int(self.stepCounter / 60))
            self.dataInfected.append(j)
            self.dataHealthy.append(k)
            self.dataDead.append(l)


    # function searches for collisions with infected particles and overwrites particles state with a given possibility to "infected"
    # def detectCollisions(self):
            # for j in range(0, len(self.particleList)):
            #     if(abs(self.particleList[i].x -self.particleList[j].x) <= self.radius and abs(self.particleList[i].y - self.particleList[j].y) <= self.radius and self.particleList[i].state == "healthy" and self.particleList[j].state == "infected"): #and self.particleList[j].state == "infected"
            #         infectionRate = self.infectionRate #Percent
            #         rndm = random.randint(1, 100)
            #         #print(rndm)
            #         if(rndm <= infectionRate):
            #             self.particleList[i].state = "infected"

    # sets the infection rate
    def setInfectionRate(self, infectionRate):
        self.infectionRate = infectionRate

    # sets the infection rate
    def setDeathRate(self, deathRate):
        self.deathRate = deathRate

    # sets the simulations radius
    def setRadius(self, radius):
        self.radius = radius
    # returns the current frame count
    def getData(self):
        return np.array([self.dataX, self.dataHealthy, self.dataInfected, self.dataDead]).T

    # returns the particleList
    def getParticles(self):
        return self.particleList