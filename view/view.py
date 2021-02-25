from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPen, QBrush
from PyQt5.QtWidgets import QSlider
import numpy as np

import pyqtgraph as pg

from view.mainwindow import Ui_MainWindow
from view.dialogCSV import DialogCSV
from view.dialogMultipleSim import DialogMultipleSim

import resources.constants as constants

ELLIPSIS_DIMENSION = 3
SCENE_DIMENSION = 200


class View(QtWidgets.QMainWindow, Ui_MainWindow):
    startSimulationSignal = QtCore.pyqtSignal(int, int, int, int, int, int, int, int, int, int, int, int, int, bool,
                                              int, int, bool)
    pauseResumeSimulationSignal = QtCore.pyqtSignal()
    resetSimulationSignal = QtCore.pyqtSignal()
    speedSimulationSignal = QtCore.pyqtSignal(float)
    infectionRateSignal = QtCore.pyqtSignal(int)
    deathRateSignal = QtCore.pyqtSignal(int)
    infectionRadiusChangedSignal = QtCore.pyqtSignal(int)
    export_csvSignal = QtCore.pyqtSignal()
    stayAtHomeSignal = QtCore.pyqtSignal()
    particleRadiusChangedSignal = QtCore.pyqtSignal(int)
    minDaysInfectedSignal = QtCore.pyqtSignal(int)
    maxDaysInfectedSignal = QtCore.pyqtSignal(int)
    percentageImmuneSignal = QtCore.pyqtSignal(int)
    minImmuneDurationSignal = QtCore.pyqtSignal(int)
    maxImmuneDurationSignal = QtCore.pyqtSignal(int)
    quarantinePercentageSignal = QtCore.pyqtSignal(int)
    multipleSimulationSignal = QtCore.pyqtSignal(int, int, int, int, int, int, int, int, int, int, int, int, int, int,
                                                 bool, int, int, bool, DialogMultipleSim)

    def __init__(self):
        """creates the gui and therefore the view.
        It also initializes all of the widgets to their initial value"""
        super(View, self).__init__()
        self.setupUi(self)
        self.connectSignals()

        # set initial configurations for the speed slider
        self.horizontalSlider.setMinimum(2)
        self.horizontalSlider.setMaximum(30)
        self.horizontalSlider.setValue(10)
        self.horizontalSlider.setTickInterval(2)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)

        # set initial configurations for the spinBoxes
        self.spinBox_particlesAmount.setMaximum(1000)
        self.spinBox_particlesAmount.setValue(100)
        self.spinBox_infectionRate.setValue(12)
        self.spinBox_infectionRadius.setValue(5)
        self.spinBox_deathRate.setValue(5)
        self.spinBox_initiallyInfected.setValue(5)
        self.spinBox_minInfectionDuration.setValue(10)
        self.spinBox_maxInfectionDuration.setValue(20)
        self.spinBox_percentageImmune.setValue(70)
        self.spinBox_minImmuneDuration.setValue(20)
        self.spinBox_maxImmuneDuration.setValue(40)
        self.spinBox_quarantinePercentage.setValue(25)

        # sets a counter
        self.counter = 0

        # setup the data
        self.dataX = []
        self.dataInfected = []
        self.dataHealthy = []
        self.dataDead = []
        self.dataImmune = []
        self.dataVaccinated = []

        # set initial configuration for the graphWidget
        # self.graphWidget.setBackground('w')
        self.graphWidget.addLegend()
        self.graphWidget.setLabel('left', constants.COUNT_OF_PARTICLES)
        self.graphWidget.setLabel('bottom', constants.TIME_IN_SECONDS)
        self.plotInfected = self.graphWidget.plot(self.dataX, self.dataInfected,
                                                  pen=pg.mkPen(color=(255, 0, 0), width=3), name=constants.HEALTHY_NAME)
        self.plotHealthy = self.graphWidget.plot(self.dataX, self.dataHealthy, pen=pg.mkPen(color=(0, 255, 0), width=3),
                                                 name=constants.INFECTED_NAME)
        self.plotDead = self.graphWidget.plot(self.dataX, self.dataDead, pen=pg.mkPen(color=(255, 255, 255), width=3),
                                              name=constants.DEAD_NAME)
        self.plotImmune = self.graphWidget.plot(self.dataX, self.dataImmune, pen=pg.mkPen(color=(255, 255, 0), width=3),
                                                name=constants.IMMUNE_NAME)
        self.plotVaccinated = self.graphWidget.plot(self.dataX, self.dataVaccinated,
                                                    pen=pg.mkPen(color=(0, 0, 255), width=3),
                                                    name=constants.VACCINATED_NAME)

    def connectSignals(self):
        """this function is used to connect all of the event handlers for the gui with functions in the view"""
        self.startSimButton.pressed.connect(self.startSimulationClicked)
        self.pauseSimButton.pressed.connect(self.pauseSimulationClicked)
        self.resetSimButton.pressed.connect(self.resetSimulationClicked)
        self.horizontalSlider.valueChanged.connect(self.speedSimulationChanged)
        self.spinBox_infectionRate.valueChanged.connect(self.infectionRateBoxChanged)
        self.spinBox_infectionRadius.valueChanged.connect(self.infectionRadiusBoxChanged)
        self.actionExport_CSV.triggered.connect(self.export_csvClicked)
        self.spinBox_deathRate.valueChanged.connect(self.deathRateBoxChanged)
        self.checkBox_peopleStayAtHome.clicked.connect(self.stayAtHomeClicked)
        self.spinBox_distanceRadius.valueChanged.connect(self.particleRadiusChanged)
        self.spinBox_minInfectionDuration.valueChanged.connect(self.minDaysInfectedChanged)
        self.spinBox_maxInfectionDuration.valueChanged.connect(self.maxDaysInfectedChanged)
        self.spinBox_percentageImmune.valueChanged.connect(self.percentageImmuneChanged)
        self.spinBox_maxImmuneDuration.valueChanged.connect(self.maxImmuneDurationChanged)
        self.spinBox_minImmuneDuration.valueChanged.connect(self.minImmuneDurationChanged)
        self.spinBox_quarantinePercentage.valueChanged.connect(self.quarantinePercentageChanged)
        self.actionMehrere_Simulationen_ausf_hren.triggered.connect(self.multipleSimDialog)

    def quarantinePercentageChanged(self):
        """emits quarantinePercentageSignal with the value of spinBox_quarantinePercentage"""
        self.quarantinePercentageSignal.emit(self.spinBox_quarantinePercentage.value())

    def maxImmuneDurationChanged(self):
        """emits maxImmuneDurationSignal with the value of spinBox_maxImmuneDuration"""
        self.maxImmuneDurationSignal.emit(self.spinBox_maxImmuneDuration.value())

    def minImmuneDurationChanged(self):
        """emits minImmuneDurationSignal with the value of spinBox_minImmuneDuration"""
        self.minImmuneDurationSignal.emit(self.spinBox_minImmuneDuration.value())

    def percentageImmuneChanged(self):
        """emits percentageImmuneSignal with the value of spinBox_percentageImmune"""
        self.percentageImmuneSignal.emit(self.spinBox_percentageImmune.value())

    def minDaysInfectedChanged(self):
        """emits minDaysInfectedSignal with the value of spinBox_minInfectionDuration"""
        self.minDaysInfectedSignal.emit(self.spinBox_minInfectionDuration.value())

    def maxDaysInfectedChanged(self):
        """emits axDaysInfectedSignal with the value of spinBox_maxInfectionDuration"""
        self.maxDaysInfectedSignal.emit(self.spinBox_maxInfectionDuration.value())

    def particleRadiusChanged(self):
        """emits particleRadiusChangedSignal with the value of spinBox_distanceRadius"""
        self.particleRadiusChangedSignal.emit(self.spinBox_distanceRadius.value())

    def startSimulationClicked(self):
        """emits the particleRadiusChangedSignal with the value of:
            SCENE_DIMENSION - ELLIPSIS_DIMENSION: maximum to move to the right,
            SCENE_DIMENSION - ELLIPSIS_DIMENSION: maximum to move down,
            spinBox_percentageImmune,
            spinBox_minImmuneDuration,
            spinBox_maxImmuneDuration,
            spinBox_particlesAmount,
            spinBox_infectionRate,
            spinBox_infectionRadius,
            spinBox_initiallyInfected,
            spinBox_deathRate,
            spinBox_minInfectionDuration,
            spinBox_maxInfectionDuration,
            spinBox_quarantinePercentage,
            checkBox_activateVaccination,
            spinBox_dateForVaccine,
            spinBox_vaccineSpeed,
            checkBox_healthyFirstVaccinated
            """
        self.startSimulationSignal.emit(SCENE_DIMENSION - ELLIPSIS_DIMENSION, SCENE_DIMENSION - ELLIPSIS_DIMENSION,
                                        self.spinBox_percentageImmune.value(), self.spinBox_minImmuneDuration.value(),
                                        self.spinBox_maxImmuneDuration.value(), self.spinBox_particlesAmount.value(),
                                        self.spinBox_infectionRate.value(), self.spinBox_infectionRadius.value(),
                                        self.spinBox_initiallyInfected.value(), self.spinBox_deathRate.value(),
                                        self.spinBox_minInfectionDuration.value(),
                                        self.spinBox_maxInfectionDuration.value(),
                                        self.spinBox_quarantinePercentage.value(),
                                        self.checkBox_activateVaccination.isChecked(),
                                        self.spinBox_dateForVaccine.value(), self.spinBox_vaccineSpeed.value(),
                                        self.checkBox_healthyFirstVaccinated.isChecked())

    def pauseSimulationClicked(self):
        """emits pauseResumeSimulationSignal"""
        self.pauseResumeSimulationSignal.emit()

    def resetSimulationClicked(self):
        """emits resetSimulationSignal"""
        self.resetSimulationSignal.emit()

    def speedSimulationChanged(self):
        """emits speedSimulationSignal with value of horizontalSlider
        Additionaly sets label_speedFactor text to a new factor of speed"""
        self.speedSimulationSignal.emit(self.horizontalSlider.value() / 10)
        self.label_speedFactor.setText("x" + str(self.horizontalSlider.value() / 10))

    def infectionRateBoxChanged(self):
        """emits infectionRateSignal with value of spinBox_infectionRate"""
        self.infectionRateSignal.emit(self.spinBox_infectionRate.value())

    def deathRateBoxChanged(self):
        """emits deathRateSignal with value of spinBox_deathRate"""
        self.deathRateSignal.emit(self.spinBox_deathRate.value())

    def infectionRadiusBoxChanged(self):
        """emits infectionRadiusChangedSignal with value of spinBox_infectionRadius"""
        self.infectionRadiusChangedSignal.emit(self.spinBox_infectionRadius.value())

    def stayAtHomeClicked(self):
        """emits stayAtHomeSignal"""
        self.stayAtHomeSignal.emit()

    def export_csvClicked(self):
        """emits export_csvSignal"""
        self.export_csvSignal.emit()

    def ask_granularity(self):
        """opens a dialog for the user to enter a given granularity for the export"""
        self.d = DialogCSV()
        self.d.finishedSignal.connect(self.export_csv)
        self.d.exec_()

    def export_csv(self, granularity):
        """function to export a csv file of the gathered data within the simulation. The function opens
        a FileDialog for the user to enter a path to save the csv file"""
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        print(name[0])
        csvMatrix = np.array(
            [self.dataX, self.dataHealthy, self.dataImmune, self.dataInfected, self.dataDead, self.dataVaccinated]).T
        np.savetxt(name[0], csvMatrix[0::granularity], delimiter=",", fmt='%i', header=constants.CSV_HEADER)

    def multipleSimDialog(self):
        """this function opens the multiple simulations dialog"""
        self.d = DialogMultipleSim()
        self.d.finishedSignal.connect(self.runMultipleSimulations)
        self.d.exec_()

    def runMultipleSimulations(self, simCount, simDuration, particlesCount, infectedParticlesCount, infectionRate,
                               infectionRadius, deathRate, minInfectionDuration, maxInfectionDuration, percentageImmune,
                               minImmuneDuration, maxImmuneDuration, distanceRadius, quarantinePercentage,
                               vaccinationActivated, vaccinationDate, vaccinationSpeed, vaccinateHealthyFirst, dialog):
        """this function emits the multipleSimulationSignal.
        Args:
            simCount: the count of simulations running simultaneously
            simDuration: the count of days the simulations will be running
            countParticles: the number of particles the simulation should hold
            initiallyInfected: the initial number of particles that are infected by the start of the simulation
            infectionRate: the initially set infection rate which with particles can infect each other
            infectionRadius: the initially set infection radius, which is used to detect collisions of the particles
            deathRate: the initially set death rate within the simulation
            minDaysInfected: the minimum of days particles have to be infected
            maxDaysInfected the maximum of days particles can be infected
            percentageImmune: the percentage of being immune after recovery
            minImmuneDuration: the minimum duration of being immune
            maxImmuneDuration: the maximum duration of being immune
            distanceRadius: the radius particles hold to each other to be on distance
            quarantinePercentage: the percentage of particles being in quarantine when infected
            vaccinationActivated: whether vaccination is activated in the current simulation
            vaccinationDate: the start of vaccination in days
            vaccinationSpeed: the count of particles being able to be vaccinated in one day
            vaccinateHealthyFirst: whether the first one getting vaccinated are the healthy ones
            dialog: the dialog from where the call came
        """
        self.multipleSimulationSignal.emit(simCount, simDuration, particlesCount, infectedParticlesCount, infectionRate,
                                           infectionRadius, deathRate, minInfectionDuration, maxInfectionDuration,
                                           percentageImmune,
                                           minImmuneDuration, maxImmuneDuration, distanceRadius, quarantinePercentage,
                                           vaccinationActivated, vaccinationDate, vaccinationSpeed,
                                           vaccinateHealthyFirst, dialog)

    def showAlert(self, message):
        """this function shows an alert to the user
        Args:
            message: the message that should be show to the user
        """
        dlg = QtWidgets.QDialog(self)
        dlg.setWindowTitle(constants.ERROR)
        label = QtWidgets.QLabel(dlg)
        label.setText(message)
        label.adjustSize()
        label.move(100, 60)
        dlg.exec_()

    def pauseSimulation(self):
        """this function changes the text of pauseSimButton to Weiter"""
        self.pauseSimButton.setText(constants.CONTINUE)

    def startSimulation(self):
        """this function clears the graphWidget and initiates arrays that hold the data while the simulation is
        processing"""
        self.graphWidget.clear()
        self.dataDead = []
        self.dataHealthy = []
        self.dataInfected = []
        self.dataX = []
        self.dataImmune = []
        self.dataVaccinated = []
        self.graphWidget.addLegend()
        self.plotInfected = self.graphWidget.plot(self.dataX, self.dataInfected,
                                                  pen=pg.mkPen(color=(255, 0, 0), width=3),
                                                  name=constants.INFECTED_NAME)
        self.plotHealthy = self.graphWidget.plot(self.dataX, self.dataHealthy, pen=pg.mkPen(color=(0, 255, 0), width=3),
                                                 name=constants.HEALTHY_NAME)
        self.plotDead = self.graphWidget.plot(self.dataX, self.dataDead, pen=pg.mkPen(color=(255, 255, 255), width=3),
                                              name=constants.DEAD_NAME)
        self.plotImmune = self.graphWidget.plot(self.dataX, self.dataImmune, pen=pg.mkPen(color=(255, 255, 0), width=3),
                                                name=constants.IMMUNE_NAME)
        self.plotVaccinated = self.graphWidget.plot(self.dataX, self.dataVaccinated,
                                                    pen=pg.mkPen(color=(0, 0, 255), width=3),
                                                    name=constants.VACCINATED_NAME)

    def resumeSimulation(self):
        """this function changes the text of pauseSimButton to Pause"""
        self.pauseSimButton.setText(constants.PAUSE)

    def resetSimulation(self):
        """this function resets the simulation by clearing the scene and the graphWidget and reinitialising the data"""
        self.graphicsView.scene().clear()
        self.graphWidget.clear()
        self.dataDead = []
        self.dataHealthy = []
        self.dataInfected = []
        self.dataX = []
        self.dataImmune = []
        self.graphWidget.addLegend()
        self.plotInfected = self.graphWidget.plot(self.dataX, self.dataInfected,
                                                  pen=pg.mkPen(color=(255, 0, 0), width=3),
                                                  name=constants.INFECTED_NAME)
        self.plotHealthy = self.graphWidget.plot(self.dataX, self.dataHealthy, pen=pg.mkPen(color=(0, 255, 0), width=3),
                                                 name=constants.HEALTHY_NAME)
        self.plotDead = self.graphWidget.plot(self.dataX, self.dataDead, pen=pg.mkPen(color=(255, 255, 255), width=3),
                                              name=constants.DEAD_NAME)
        self.plotImmune = self.graphWidget.plot(self.dataX, self.dataImmune, pen=pg.mkPen(color=(255, 255, 0), width=3),
                                                name=constants.IMMUNE_NAME)
        self.plotVaccinated = self.graphWidget.plot(self.dataX, self.dataVaccinated,
                                                    pen=pg.mkPen(color=(0, 0, 255), width=3),
                                                    name=constants.VACCINATED_NAME)

    # function visualizes the data from the simulation model in a graphicsview. It uses a new scene for every step.
    def updateParticles(self, particleList, data):
        """this function visualizes the retrieved data from the simulation model in a graphview.
        For every step a new scene is used.

        Args:
            particleList: the list that stores all of the particles that should be drawn
            data: an array of all of the data that holds statistics to the current simulation
        """
        scene = QtWidgets.QGraphicsScene(0, 0, SCENE_DIMENSION, SCENE_DIMENSION)  # scene with 200 x 200 size
        for i in range(0, len(particleList)):
            if (particleList[i].state == constants.HEALTHY):
                pen = QPen(Qt.darkGreen)
                brush = QBrush(Qt.green)
            elif (particleList[i].state == constants.INFECTED):
                pen = QPen(Qt.darkRed)
                brush = QBrush(Qt.red)
            elif (particleList[i].state == constants.IMMUNE):
                pen = QPen(Qt.darkYellow)
                brush = QBrush(Qt.yellow)
            elif (particleList[i].state == constants.VACCINATED):
                pen = QPen(Qt.darkCyan)
                brush = QBrush(Qt.cyan)
            else:  # == constants.DEAD
                pen = QPen(Qt.gray)
                brush = QBrush(Qt.white)
            scene.addEllipse(
                QRectF(particleList[i].x - ELLIPSIS_DIMENSION / 2, particleList[i].y - ELLIPSIS_DIMENSION / 2,
                       ELLIPSIS_DIMENSION, ELLIPSIS_DIMENSION), pen, brush)
            if self.actionShow_InfectionRadius.isChecked() and particleList[i].state == constants.INFECTED:
                # draws an infection circe around particles for debugging purposes
                scene.addEllipse(
                    QRectF(particleList[i].x - ELLIPSIS_DIMENSION / 2 - self.spinBox_infectionRadius.value(),
                           particleList[i].y - ELLIPSIS_DIMENSION / 2 - self.spinBox_infectionRadius.value(),
                           self.spinBox_infectionRadius.value() * 2 + ELLIPSIS_DIMENSION,
                           self.spinBox_infectionRadius.value() * 2 + ELLIPSIS_DIMENSION), pen)
            if self.actionShow_DistanceRadius.isChecked():
                # draws a distance circle around particles for debugging purposes
                scene.addEllipse(
                    QRectF(particleList[i].x - ELLIPSIS_DIMENSION / 2 - self.spinBox_distanceRadius.value(),
                           particleList[i].y - ELLIPSIS_DIMENSION / 2 - self.spinBox_distanceRadius.value(),
                           self.spinBox_distanceRadius.value() * 2 + ELLIPSIS_DIMENSION,
                           self.spinBox_distanceRadius.value() * 2 + ELLIPSIS_DIMENSION), QPen(Qt.magenta))
        self.graphicsView.setScene(scene)
        self.graphicsView.ensureVisible(scene.sceneRect())
        self.graphicsView.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
        self.counter += 1
        # retrieving data from the model for the graph
        if (self.counter % 60 == 0):
            self.dataX = data[:, 0]
            self.dataHealthy = data[:, 1]
            self.dataInfected = data[:, 3]
            self.dataDead = data[:, 4]
            self.dataImmune = data[:, 2]
            self.dataVaccinated = data[:, 5]
            self.plotInfected.setData(self.dataX, self.dataInfected)
            self.plotHealthy.setData(self.dataX, self.dataHealthy)
            self.plotDead.setData(self.dataX, self.dataDead)
            self.plotImmune.setData(self.dataX, self.dataImmune)
            self.plotVaccinated.setData(self.dataX, self.dataVaccinated)
