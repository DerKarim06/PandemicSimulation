from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPen, QBrush
from PyQt5.QtWidgets import QSlider
import numpy as np
import random

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from view.dialogwindowMultipleSim import Ui_Dialog
import resources.constants as constants

COLORS = [(255, 0, 0), (255, 255, 0), (255, 0, 255), (0, 255, 0), (0, 255, 255), (0, 0, 255), (142, 80, 33),
          (15, 178, 56), (45, 76, 41), (98, 213, 145), (145, 100, 246), (27, 164, 60)]

class DialogMultipleSim(QtWidgets.QDialog, Ui_Dialog):

    finishedSignal = QtCore.pyqtSignal(int, int, int, int, int, int, int, int, int, int, int, int, int, int, Ui_Dialog)

    def __init__(self):
        super(DialogMultipleSim, self).__init__()
        self.setupUi(self)
        self.connectSignals()

        self.counter = 0

        self.dataX = []
        self.dataInfected = []
        self.dataHealthy = []
        self.dataDead = []
        self.dataImmune = []

        self.plots = [[], [], [], []]

        self.colors = []

    def connectSignals(self):
        self.pushButton.clicked.connect(self.okClicked)

    def okClicked(self):
        print("clicked")

        self.counter = 0

        self.dataX = []
        self.dataInfected = []
        self.dataHealthy = []
        self.dataDead = []
        self.dataImmune = []

        self.plots = [[], [], [], []]

        self.colors = []

        # set initial configuration for the graphWidget
        # self.graphWidget.setBackground('w')
        self.graphWidget_2.clear()
        self.graphWidget_2.setLabel('left', constants.COUNT_OF_PARTICLES)
        self.graphWidget_2.setLabel('bottom', constants.TIME_IN_SECONDS)
        self.graphWidget_2.setTitle("Gesunde Partikel", color="w", size="25pt")
        self.graphWidget_3.clear()
        self.graphWidget_3.setLabel('left', constants.COUNT_OF_PARTICLES)
        self.graphWidget_3.setLabel('bottom', constants.TIME_IN_SECONDS)
        self.graphWidget_3.setTitle("Infizierte Partikel", color="w", size="25pt")
        self.graphWidget_4.clear()
        self.graphWidget_4.setLabel('left', constants.COUNT_OF_PARTICLES)
        self.graphWidget_4.setLabel('bottom', constants.TIME_IN_SECONDS)
        self.graphWidget_4.setTitle("Immune Partikel", color="w", size="25pt")
        self.graphWidget_5.clear()
        self.graphWidget_5.setLabel('left', constants.COUNT_OF_PARTICLES)
        self.graphWidget_5.setLabel('bottom', constants.TIME_IN_SECONDS)
        self.graphWidget_5.setTitle("Tote Partikel", color="w", size="25pt")

        for i in range(0, self.spinBox.value()):

            self.dataInfected.append([])
            self.dataHealthy.append([])
            self.dataDead.append([])
            self.dataImmune.append([])
            self.colors.append(random.randint(0, len(COLORS)-1))
            self.plots[0].append(self.graphWidget_2.plot(self.dataX, self.dataHealthy[i],
                                                      pen=pg.mkPen(color=self.colors[i], width=3)))
            self.plots[1].append(self.graphWidget_3.plot(self.dataX, self.dataInfected[i],
                                                         pen=pg.mkPen(color=self.colors[i], width=3)))
            self.plots[2].append(self.graphWidget_4.plot(self.dataX, self.dataImmune[i],
                                                         pen=pg.mkPen(color=self.colors[i], width=3)))
            self.plots[3].append(self.graphWidget_5.plot(self.dataX, self.dataDead[i],
                                                         pen=pg.mkPen(color=self.colors[i], width=3)))


        self.finishedSignal.emit(self.spinBox.value(), self.spinBox_2.value(), self.spinBox_3.value(),
                                 self.spinBox_4.value(), self.spinBox_8.value(), self.spinBox_9.value(),
                                 self.spinBox_10.value(), self.spinBox_11.value(), self.spinBox_12.value(),
                                 self.spinBox_5.value(), self.spinBox_6.value(), self.spinBox_7.value(),
                                 self.spinBox_13.value(), self.spinBox_14.value(), self)


    def updateData(self, data):
        self.counter += 1
        print(data[0][:, 1])
        print(self.counter)
        if self.counter % 60 == 0:
            print(len(self.plots[0]))
            for i in range(0, len(self.plots[0])):
                self.dataX = data[0][:, 0]
                self.dataHealthy[i] = data[i][:, 1]
                self.dataInfected[i] = data[i][:, 3]
                self.dataDead[i] = data[i][:, 4]
                self.dataImmune[i] = data[i][:, 2]
                self.plots[0][i].setData(self.dataX, self.dataHealthy[i])
                self.plots[1][i].setData(self.dataX, self.dataInfected[i])
                self.plots[2][i].setData(self.dataX, self.dataImmune[i])
                self.plots[3][i].setData(self.dataX, self.dataDead[i])
