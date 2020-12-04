from PyQt5.QtCore import QRectF

from model.particle import Particle
# from model.particleState import ParticleState
# from model.statistics import Statistics
import random

from PyQt5 import QtWidgets


class Simulation:
    def __init__(self):
        print("Simulation Created")
        self.stepCounter = 0
        self.scene = QtWidgets.QGraphicsScene(0, 0, 500, 500)

        rect1 = self.scene.addRect(QRectF(0, 0, 100, 100))
        rect2 = self.scene.addRect(QRectF(0, 20, 100, 100))

        print(rect1.collidesWithItem(rect2))
        print(len(rect1.collidingItems()))

        # for i in range(0, 1):
        #     rndmX = random.randint(0, 500)
        #     rndmY = random.randint(0, 500)
        #     particle = Particle(rndmX, rndmY)
        #     p1 = Particle(12, 12)
        #     p2 = Particle(13, 13)
        #     print(p1.collidesWithItem(p2))
        #     print(len(p1.collidingItems()))
        #     if(len(particle.collidingItems()) > 0):
        #         i = i - 1
        #     else:
        #         self.scene.addItem(particle)

    def performStep(self):
        self.stepCounter += 1
        print("Simulation step {} processed.".format(self.stepCounter))


    def getData(self):
        return self.stepCounter

    def getScene(self):
        return self.scene