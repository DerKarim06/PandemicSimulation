from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QPen, QBrush

from model.particle import Particle
# from model.particleState import ParticleState
# from model.statistics import Statistics
import random

from PyQt5 import QtWidgets


class Simulation:
    def __init__(self):
        print("Simulation Created")
        self.stepCounter = 0
        self.scene = QtWidgets.QGraphicsScene(0, 0, 200, 200)
        self.rectList = {}
        test1 = self.scene.addRect(QRectF(0, 0, 5, 5), QPen(Qt.darkRed), QBrush(Qt.red))
        test2 = self.scene.addRect(QRectF(195, 195, 5, 5), QPen(Qt.darkRed), QBrush(Qt.red))

        self.rectList[101] = test1

        print(test1.scenePos().x())
        print(self.scene.width())

        print(test2.scenePos().x())
        print(test2.rect().x())
        print(test1.rect().y() - 1)

        for i in range(0, 100):
            rndmX = random.randint(0, 200)
            rndmY = random.randint(0, 200)
            # particle = Particle(rndmX, rndmY)
            # print(self.scene.collidingItems(particle, mode=Qt.IntersectsItemBoundingRect))
            # self.rectList[i] = self.scene.addItem(particle)
            self.rectList[i] = self.scene.addRect(QRectF(rndmX, rndmY, 5, 5), QPen(Qt.darkGreen), QBrush(Qt.green))
            if(len(self.rectList[i].collidingItems()) > 0):
                self.rectList[i].hide()
                i = i - 1

    def performStep(self):
        self.stepCounter += 1
        print("Simulation step {} processed.".format(self.stepCounter))
        for i in range(0, 100):
            rndm = random.randint(1, 4) # 1: down, 2: up, 3: left, 4: right
            x = self.rectList[i].rect().x() + self.rectList[i].scenePos().x()
            y = self.rectList[i].rect().y() + self.rectList[i].scenePos().y()
            if(rndm == 1 and y < 200 - 5):
                self.rectList[i].moveBy(0, 1)
                if(len(self.rectList[i].collidingItems()) > 0):
                    self.rectList[i].setBrush(Qt.red)
                    self.rectList[i].setPen(Qt.darkRed)
            elif(rndm == 2 and y > 0):
                self.rectList[i].moveBy(0, -1)
                if (len(self.rectList[i].collidingItems()) > 0):
                    self.rectList[i].setBrush(Qt.red)
                    self.rectList[i].setPen(Qt.darkRed)
            elif(rndm == 3 and x > 0):
                self.rectList[i].moveBy(-1, 0)
                if (len(self.rectList[i].collidingItems()) > 0):
                    self.rectList[i].setBrush(Qt.red)
                    self.rectList[i].setPen(Qt.darkRed)
            elif (rndm == 4 and x < 200 - 5):
                self.rectList[i].moveBy(1, 0)
                if (len(self.rectList[i].collidingItems()) > 0):
                    self.rectList[i].setBrush(Qt.red)
                    self.rectList[i].setPen(Qt.darkRed)
            else:
                i = i - 1


    def getData(self):
        return self.stepCounter

    def getScene(self):
        return self.scene