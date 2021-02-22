import numpy as np
import random

from model.particle import Particle

import resources.constants as constants

FRAMES_FOR_ONE_DAY = 60

class Simulation:
    """This class represents the whole simulation holding all of the particles"""
    def __init__(self, xBorder, yBorder, percentageImmune, minImmuneDuration, maxImmuneDuration, countParticles=100, infectionRate=12, infectionRadius=5, initiallyInfected=1, deathRate=8, minDaysInfected=10, maxDaysInfected=20, quarantinePercentage=25):
        """this is the constructor of the simulation class. The simulation additionally holds lists in which the
        simulations data is stored for future exports

        Args:
            xBorder: the maximum x-coordinate particles are allowed to move to the right
            yBorder: the maximum y-coordinate particles are allowed to move down
            percentageImmune: the percentage of being immune after recovery
            minImmuneDuration: the minimum duration of being immune
            maxImmuneDuration: the maximum duration of being immune
            countParticles: the number of particles the simulation should hold (default: 100)
            infectionRate: the initially set infection rate which with particles can infect each other (default: 12)
            infectionRadius: the initially set infection radius, which is used to detect collisions of the particles (default: 5)
            initiallyInfected: the initial number of particles that are infected by the start of the simulation (default: 1)
            deathRate: the initially set death rate within the simulation (default: 8)
            minDaysInfected: the minimum of days particles have to be infected (default: 10)
            maxDaysInfected the maximum of day particles can be infected up to (default: 20)
            quarantinePercentage: the percentage of particles being in quarantine when infected (default: 25)
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
            self.particleList[i].state = constants.INFECTED # initially set particles state as "infected"

        self.dataX = [0]
        self.dataInfected = [initiallyInfected]
        self.dataHealthy = [countParticles - initiallyInfected]
        self.dataImmune = [0]
        self.dataDead = [0]

        self.minDaysInfected = minDaysInfected
        self.maxDaysInfected = maxDaysInfected

        self.percentageImmune = percentageImmune
        self.maxImmuneDuration = maxImmuneDuration
        self.minImmuneDuration = minImmuneDuration

        self.quarantinePercentage = quarantinePercentage

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
        m = 0
        for i in range(0, len(self.particleList)):
            self.particleList[i].detect_collisions(self.particleList[i:], self.infectionRate, self.infectionRadius)
        for i in range(0, len(self.particleList)):
            if(self.particleList[i].state != constants.DEAD):
                self.particleList[i].move()
            if self.particleList[i].state == constants.INFECTED:
                self.particleList[i].incrementInfectionCounter()
            if self.particleList[i].state == constants.IMMUNE:
                self.particleList[i].incrementImmuneCounter()
            if (self.stepCounter % FRAMES_FOR_ONE_DAY == 0): #Find variables for the statistic/csv
                if (self.particleList[i].state == constants.DEAD):
                    l += 1
                if (self.particleList[i].state == constants.INFECTED):
                    j += 1
                if (self.particleList[i].state == constants.IMMUNE):
                    m += 1
                if (self.particleList[i].state == constants.HEALTHY):
                    k += 1
        if (self.stepCounter % FRAMES_FOR_ONE_DAY == 0): #add the variables to the lists
            self.dataX.append(int(self.stepCounter / FRAMES_FOR_ONE_DAY))
            self.dataInfected.append(j)
            self.dataHealthy.append(k)
            self.dataImmune.append(m)
            self.dataDead.append(l)
        print("test")

    def setMaxImmuneDuration(self, duration):
        """sets the maximum duration of particle allowed to be immune
        Args:
            duration: the new maximum duration of particles being allowed to be immune
        """
        self.maxImmuneDuration = duration

    def setQuarantinePercentage(self, percentage):
        """sets the percentage of particles that are in quarantine while being infected
        Args:
            percentage: the new percentage of quarantining particles
        """
        self.quarantinePercentage = percentage

    def setMinImmuneDuration(self, duration):
        """sets the minimum duration of particle allowed to be immune
        Args:
            duration: the new minimum duration of particles being allowed to be immune
        """
        self.minImmuneDuration = duration

    def setPercentageImmune(self, percentage):
        """sets the percentage of particle being immune after recovery
        Args:
            percentage: the new percentage of being immune after recovery
        """
        self.percentageImmune = percentage

    def getPercentageImmune(self):
        """get method of current percentage of being immune after recovery
        Returns:
            current percentage of being immune after recovery
        """
        return self.percentageImmune

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
        return np.array([self.dataX, self.dataHealthy, self.dataImmune, self.dataInfected, self.dataDead]).T

    def getParticles(self):
        """this function returns the particle list
        Returns:
            the particle list where all of the particles are stored"""
        return self.particleList