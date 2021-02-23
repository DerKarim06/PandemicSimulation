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

    finishedSignal = QtCore.pyqtSignal(int, int, int, int, int, int, int, int, int, int, int, int, int, int, bool, int, int, bool, Ui_Dialog)

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
        self.dataVaccinated = []

        self.plots = [[], [], [], [], []]

        self.colors = []

        self.spinBox_countSim.setValue(4)
        self.spinBox_simDuration.setValue(25)
        self.spinBox_countParticles.setValue(99)
        self.spinBox_countInfectedParticles.setValue(3)
        self.spinBox_infectionRate.setValue(60)
        self.spinBox_infectionRadius.setValue(5)
        self.spinBox_deathRate.setValue(5)
        self.spinBox_minInfectionDays.setValue(7)
        self.spinBox_maxInfectionDays.setValue(16)
        self.spinBox_ImmunePercentage.setValue(30)
        self.spinBox_minImmuneDays.setValue(5)
        self.spinBox_maxImmuneDays.setValue(15)
        self.spinBox_quarantinePercentage.setValue(20)

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
        self.dataVaccinated = []

        self.plots = [[], [], [], [], []]

        self.colors = []

        # set initial configuration for the graphWidget
        # self.graphWidget.setBackground('w')
        self.graphWidget_Healthy.clear()
        self.graphWidget_Healthy.setLabel('left', constants.COUNT_OF_PARTICLES)
        self.graphWidget_Healthy.setLabel('bottom', constants.TIME_IN_SECONDS)
        self.graphWidget_Healthy.setTitle("Gesunde Partikel", color="w", size="25pt")
        self.graphWidget_Infected.clear()
        self.graphWidget_Infected.setLabel('left', constants.COUNT_OF_PARTICLES)
        self.graphWidget_Infected.setLabel('bottom', constants.TIME_IN_SECONDS)
        self.graphWidget_Infected.setTitle("Infizierte Partikel", color="w", size="25pt")
        self.graphWidget_Immune.clear()
        self.graphWidget_Immune.setLabel('left', constants.COUNT_OF_PARTICLES)
        self.graphWidget_Immune.setLabel('bottom', constants.TIME_IN_SECONDS)
        self.graphWidget_Immune.setTitle("Immune Partikel", color="w", size="25pt")
        self.graphWidget_Vaccinated.clear()
        self.graphWidget_Vaccinated.setLabel('left', constants.COUNT_OF_PARTICLES)
        self.graphWidget_Vaccinated.setLabel('bottom', constants.TIME_IN_SECONDS)
        self.graphWidget_Vaccinated.setTitle("Geimpfte Partikel", color="w", size="25pt")
        self.graphWidget_Dead.clear()
        self.graphWidget_Dead.setLabel('left', constants.COUNT_OF_PARTICLES)
        self.graphWidget_Dead.setLabel('bottom', constants.TIME_IN_SECONDS)
        self.graphWidget_Dead.setTitle("Tote Partikel", color="w", size="25pt")

        for i in range(0, self.spinBox_countSim.value()):

            self.dataInfected.append([])
            self.dataHealthy.append([])
            self.dataDead.append([])
            self.dataImmune.append([])
            self.dataVaccinated.append([])
            self.colors.append(random.randint(0, len(COLORS)-1))
            self.plots[0].append(self.graphWidget_Healthy.plot(self.dataX, self.dataHealthy[i],
                                                      pen=pg.mkPen(color=self.colors[i], width=3)))
            self.plots[1].append(self.graphWidget_Infected.plot(self.dataX, self.dataInfected[i],
                                                         pen=pg.mkPen(color=self.colors[i], width=3)))
            self.plots[2].append(self.graphWidget_Immune.plot(self.dataX, self.dataImmune[i],
                                                         pen=pg.mkPen(color=self.colors[i], width=3)))
            self.plots[3].append(self.graphWidget_Dead.plot(self.dataX, self.dataDead[i],
                                                         pen=pg.mkPen(color=self.colors[i], width=3)))
            self.plots[4].append(self.graphWidget_Vaccinated.plot(self.dataX, self.dataVaccinated[i],
                                                            pen=pg.mkPen(color=self.colors[i], width=3)))


        self.finishedSignal.emit(self.spinBox_countSim.value(), self.spinBox_simDuration.value(), self.spinBox_countParticles.value(),
                                 self.spinBox_countInfectedParticles.value(), self.spinBox_infectionRate.value(), self.spinBox_infectionRadius.value(),
                                 self.spinBox_deathRate.value(), self.spinBox_minInfectionDays.value(), self.spinBox_maxInfectionDays.value(),
                                 self.spinBox_ImmunePercentage.value(), self.spinBox_minImmuneDays.value(), self.spinBox_maxImmuneDays.value(),
                                 self.spinBox_distanceRadius.value(), self.spinBox_quarantinePercentage.value(), self.checkBox_activateVaccination.isChecked(), self.spinBox_dateForVaccine.value(), self.spinBox_vaccineSpeed.value(), self.checkBox_healthyFirstVaccinated.isChecked(), self)


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
                self.dataVaccinated[i] = data[i][:, 5]
                self.plots[0][i].setData(self.dataX, self.dataHealthy[i])
                self.plots[1][i].setData(self.dataX, self.dataInfected[i])
                self.plots[2][i].setData(self.dataX, self.dataImmune[i])
                self.plots[3][i].setData(self.dataX, self.dataDead[i])
                self.plots[4][i].setData(self.dataX, self.dataVaccinated[i])
