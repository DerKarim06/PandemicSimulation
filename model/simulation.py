from model.particle import Particle
# from model.particleState import ParticleState
# from model.statistics import Statistics
import random


class Simulation:
    def __init__(self):
        print("Simulation Created")
        self.stepCounter = 0
        self.particleList = {}
        for i in range(0, 100):
            rndmX = random.randint(0, 200)
            rndmY = random.randint(0, 200)
            self.particleList[i] = Particle(rndmX, rndmY, 5)
        #for i in range(0, 10):
        #    self.particleList[i].state = "infected"

    def performStep(self):
        self.stepCounter += 1
        print("Simulation step {} processed.".format(self.stepCounter))
        for i in range(0, len(self.particleList)):
            self.particleList[i].move()
        self.detectCollisions()

    def detectCollisions(self):
        for i in range(0, len(self.particleList)):
            for j in range(0, len(self.particleList)):
                if(self.particleList[i].x == self.particleList[j].x and self.particleList[i].y == self.particleList[j].y and self.particleList[i].state == "healthy"): #and self.particleList[j].state == "infected"
                    infectionRate = 12 #Percent
                    rndm = random.randint(1, 800)
                    if(rndm <= infectionRate):
                        self.particleList[i].state = "infected"
            if (self.particleList[i].state == "infected"):
                deathRate = 2  # Percent
                rndm = random.randint(1, 100)
                self.particleList[i].infectionCounter = self.particleList[i].infectionCounter + 1
                if (rndm <= deathRate):
                    self.particleList[i].state = "dead"
                elif(self.particleList[i].infectionCounter > 14):
                    self.particleList[i].infectionCounter = 0
                    self.particleList[i].state = "healthy"

    def getData(self):
        return self.stepCounter

    def getParticles(self):
        return self.particleList