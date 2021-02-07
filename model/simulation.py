import numpy as np
import random

from model.particle import Particle

import resources.strings as strings

FRAMES_FOR_ONE_DAY = 60

class Simulation:
    """This class represents the whole simulation holding all of the particles"""
    def __init__(self, xBorder, yBorder, countParticles=100, infectionRate=12, infectionRadius=5, initiallyInfected=1, deathRate=8, minDaysInfected=10, maxDaysInfected=20):
        """this is the constructor of the simulation class. The simulation additionally holds lists in which the
        simulations data is stored for future exports

        Args:
            xBorder: the maximum x-coordinate particles are allowed to move to the right
            yBorder: the maximum y-coordinate particles are allowed to move down
            countParticles: the number of particles the simulation should hold (default: 100)
            infectionRate: the initially set infection rate which with particles can infect each other
            infectionRadius: the initially set infection radius, which is used to detect collisions of the particles
            initiallyInfected: the initial number of particles that are infected by the start of the simulation
            deathRate: the initially set death rate within the simulation
            minDaysInfected: the minimum of days particles have to be infected
            maxDaysInfected the maximum of day particles can be infected up to
        """

        self.xBorder = xBorder
        self.yBorder = yBorder
        self.infectionRadius = infectionRadius
        self.infectionRate = infectionRate
        self.deathRate = deathRate
        self.stepCounter = 0
        self.particleList = []
        self.peopleStayAtHome = False
        # iterate through particleList and create as many particles as countParticles is. the positions are random
        for i in range(0, countParticles):
            rndmX = random.randint(0, xBorder)
            rndmY = random.randint(0, yBorder)
            self.particleList.append(Particle(rndmX, rndmY, self))
        for i in range(initiallyInfected):
            self.particleList[i].state = strings.INFECTED # initially set particles state as "infected"

        self.dataX = [0]
        self.dataInfected = [initiallyInfected]
        self.dataHealthy = [countParticles - initiallyInfected]
        self.dataDead = [0]

        self.minDaysInfected = minDaysInfected
        self.maxDaysInfected = maxDaysInfected

    def performStep(self):
        """this function is used to perform a step in the simulation. Each step is therefore an iteration
        to progress within the simulation.

        It increments the step counter on every call, detects collisions among the particles, moves them
        and eventually tracks the current state of the simulation for latter export needs
        """
        self.stepCounter += 1 # variable to know how many frames were already created
        # move every particle in particleList
        j = 0
        k = 0
        l = 0
        for i in range(0, len(self.particleList)):
            self.particleList[i].detect_collisions(self.particleList[i:], self.infectionRate, self.infectionRadius)
        for i in range(0, len(self.particleList)):
            if(self.particleList[i].state != strings.DEAD):
                self.particleList[i].move()
            if self.particleList[i].state == strings.INFECTED:
                self.particleList[i].incrementInfectionCounter()
            if (self.stepCounter % FRAMES_FOR_ONE_DAY == 0): #Find variables for the statistic/csv
                if (self.particleList[i].state == strings.DEAD):
                    l += 1
                if (self.particleList[i].state == strings.INFECTED):
                    j += 1
                if (self.particleList[i].state == strings.HEALTHY):
                    k += 1
        if (self.stepCounter % FRAMES_FOR_ONE_DAY == 0): #add the variables to the lists
            self.dataX.append(int(self.stepCounter / FRAMES_FOR_ONE_DAY))
            self.dataInfected.append(j)
            self.dataHealthy.append(k)
            self.dataDead.append(l)

    def changePeopleStayAtHome(self):
        """changes whether people change at home or not"""
        self.peopleStayAtHome = not self.peopleStayAtHome

    def setInfectionRate(self, infectionRate):
        """sets the infection rate
        Args:
            infectionRate: the new infection rate
        """
        self.infectionRate = infectionRate

    def setDeathRate(self, deathRate):
        """sets the death rate
        Args:
            deathRate: the new death rate
        """
        self.deathRate = deathRate

    def changeParticleRadius(self, radius):
        """sets the radius in every particle
        Args:
            radius: the new radius for every particle
        """
        for i in range(0, len(self.particleList)):
            self.particleList[i].setParticleRadius(radius)

    def setMinDaysInfected(self, minDaysInfected):
        """sets the minimum days particles have to be infected
        Args:
            minDaysInfected: the new minimum of days to be infected
        """
        self.minDaysInfected = minDaysInfected

    def setMaxDaysInfected(self, maxDaysInfected):
        """sets the maximum days particles are able to be infected
        Args:
            maxDaysInfected: the new maximum of days to be potentially infected
        """
        self.maxDaysInfected = maxDaysInfected

    def setinfectionRadius(self, infectionRadius):
        """sets the simulations infection radius
        Args:
            infectionRadius: the new infection radius
        """
        self.infectionRadius = infectionRadius

    def getData(self):
        """returns the data stored for export uses.
        Returns:
            a numpy array holding the count of healthy, infected and dead particles to each step count
        """
        return np.array([self.dataX, self.dataHealthy, self.dataInfected, self.dataDead]).T

    def getParticles(self):
        """this function returns the particle list
        Returns:
            the particle list where all of the particles are stored"""
        return self.particleList