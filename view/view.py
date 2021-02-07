from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPen, QBrush
from PyQt5.QtWidgets import QSlider
import numpy as np

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from view.mainwindow import Ui_MainWindow
from view.dialog import Dialog

import resources.strings as strings


ELLIPSIS_DIMENSION = 5
SCENE_DIMENSION = 200

class View(QtWidgets.QMainWindow, Ui_MainWindow):

    startSimulationSignal = QtCore.pyqtSignal(int, int, int, int, int, int, int, int, int)
    pauseResumeSimulationSignal = QtCore.pyqtSignal()
    resetSimulationSignal = QtCore.pyqtSignal()
    speedSimulationSignal = QtCore.pyqtSignal(int)
    infectionRateSignal = QtCore.pyqtSignal(int)
    deathRateSignal = QtCore.pyqtSignal(int)
    infectionRadiusChangedSignal = QtCore.pyqtSignal(int)
    export_csvSignal = QtCore.pyqtSignal()
    stayAtHomeSignal = QtCore.pyqtSignal()
    particleRadiusChangedSignal = QtCore.pyqtSignal(int)
    minDaysInfectedSignal = QtCore.pyqtSignal(int)
    maxDaysInfectedSignal = QtCore.pyqtSignal(int)

    def __init__(self):
        """create the gui and therefore the view.
        It also initializes all of the widgets to their initial value"""
        super(View, self).__init__()
        self.setupUi(self)
        self.connectSignals()
        # FPS slider
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setValue(1)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        # particle count spinbox
        self.spinBox.setMaximum(1000)
        self.spinBox.setValue(100)
        #infection rate spinbox
        self.spinBox_2.setValue(12)
        # infectionradius spinbox
        self.spinBox_3.setValue(5)
        self.i = 0
        self.j = 0

        self.spinBox_4.setValue(5)
        self.spinBox_5.setValue(5)

        self.spinBox_9.setValue(10)
        self.spinBox_10.setValue(20)

        self.dataX = []
        self.dataInfected = []
        self.dataHealthy = []
        self.dataDead = []

        #self.graphWidget.setBackground('w')
        self.graphWidget.setLabel('left', strings.COUNT_OF_PARTICLES)
        self.graphWidget.setLabel('bottom', strings.TIME_IN_SECONDS)
        self.plotInfected = self.graphWidget.plot(self.dataX, self.dataInfected, pen=pg.mkPen(color=(255, 0, 0), width=3))
        self.plotHealthy = self.graphWidget.plot(self.dataX, self.dataHealthy, pen=pg.mkPen(color=(0, 255, 0), width=3))
        self.plotDead = self.graphWidget.plot(self.dataX, self.dataDead, pen=pg.mkPen(color=(255, 255, 255), width=3))

    def connectSignals(self):
        """this function is used to connect all of the event handlers for the gui with functions in the view"""
        self.startSimButton.pressed.connect(self.startSimulationClicked)
        self.pauseSimButton.pressed.connect(self.pauseSimulationClicked)
        self.resetSimButton.pressed.connect(self.resetSimulationClicked)
        self.horizontalSlider.valueChanged.connect(self.speedSimulationChanged)
        self.spinBox_2.valueChanged.connect(self.infectionRateBoxChanged)
        self.spinBox_3.valueChanged.connect(self.infectionRadiusBoxChanged)
        self.actionExport_CSV.triggered.connect(self.export_csvClicked)
        self.spinBox_4.valueChanged.connect(self.deathRateBoxChanged)
        self.checkBox.clicked.connect(self.stayAtHomeClicked)
        self.spinBox_7.valueChanged.connect(self.particleRadiusChanged)
        self.spinBox_9.valueChanged.connect(self.minDaysInfectedChanged)
        self.spinBox_10.valueChanged.connect(self.maxDaysInfectedChanged)

    def minDaysInfectedChanged(self):
        """emits minDaysInfectedSignal with the value of spinBox_9"""
        self.minDaysInfectedSignal.emit(self.spinBox_9.value())

    def maxDaysInfectedChanged(self):
        """emits axDaysInfectedSignal with the value of spinBox_10"""
        self.maxDaysInfectedSignal.emit(self.spinBox_10.value())

    def particleRadiusChanged(self):
        """emits particleRadiusChangedSignal with the value of spinBox_7"""
        self.particleRadiusChangedSignal.emit(self.spinBox_7.value())

    def startSimulationClicked(self):
        """emits the particleRadiusChangedSignal with the value of:
            SCENE_DIMENSION - ELLIPSIS_DIMENSION: maximum to move to the right,
            SCENE_DIMENSION - ELLIPSIS_DIMENSION: maximum to move down,
            spinBox,
            spinBox_2,
            spinBox_3,
            spinBox_5,
            spinBox_4,
            spinBox_9,
            spinBox_10"""
        self.startSimulationSignal.emit(SCENE_DIMENSION - ELLIPSIS_DIMENSION, SCENE_DIMENSION - ELLIPSIS_DIMENSION, self.spinBox.value(), self.spinBox_2.value(), self.spinBox_3.value(), self.spinBox_5.value(), self.spinBox_4.value(), self.spinBox_9.value(), self.spinBox_10.value())

    def pauseSimulationClicked(self):
        """emits pauseResumeSimulationSignal"""
        self.pauseResumeSimulationSignal.emit()

    def resetSimulationClicked(self):
        """emits resetSimulationSignal"""
        self.resetSimulationSignal.emit()

    def speedSimulationChanged(self):
        """emits speedSimulationSignal with value of horizontalSlider
        Additionaly sets label_17 text to a new factor of speed"""
        self.speedSimulationSignal.emit(self.horizontalSlider.value())
        self.label_17.setText("x" + str(self.horizontalSlider.value()))

    def infectionRateBoxChanged(self):
        """emits infectionRateSignal with value of spinBox_2"""
        self.infectionRateSignal.emit(self.spinBox_2.value())

    def deathRateBoxChanged(self):
        """emits deathRateSignal with value of spinBox_4"""
        self.deathRateSignal.emit(self.spinBox_4.value())

    def infectionRadiusBoxChanged(self):
        """emits infectionRadiusChangedSignal with value of spinBox_3"""
        self.infectionRadiusChangedSignal.emit(self.spinBox_3.value())

    def stayAtHomeClicked(self):
        """emits stayAtHomeSignal"""
        self.stayAtHomeSignal.emit()

    def export_csvClicked(self):
        """emits export_csvSignal"""
        self.export_csvSignal.emit()
    
    def ask_granularity(self):
        """opens a dialog for the user to enter a given granularity for the export"""
        self.d = Dialog()
        self.d.finishedSignal.connect(self.export_csv)
        self.d.exec_()

    def export_csv(self, granularity):
        """function to export a csv file of the gathered data within the simulation. The function opens
        a FileDialog for the user to enter a path to save the csv file"""
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        print(name[0])
        csvMatrix = np.array([self.dataX, self.dataHealthy, self.dataInfected, self.dataDead]).T
        np.savetxt(name[0], csvMatrix[0::granularity], delimiter=",", fmt='%i', header=strings.CSV_HEADER)

    def showAlert(self, message):
        """this function shows an alert to the user
        Args:
            message: the message that should be show to the user
        """
        dlg = QtWidgets.QDialog(self)
        dlg.setWindowTitle(strings.ERROR)
        label = QtWidgets.QLabel(dlg)
        label.setText(message)
        label.adjustSize()
        label.move(100, 60)
        dlg.exec_()

    def pauseSimulation(self):
        """this function changes the text of pauseSimButton to Weiter"""
        self.pauseSimButton.setText(strings.CONTINUE)

    def startSimulation(self):
        """this function clears the graphWidget and initiates arrays that hold the data while the simulation is processing"""
        self.graphWidget.clear()
        self.dataDead = []
        self.dataHealthy = []
        self.dataInfected = []
        self.dataX = []
        self.plotInfected = self.graphWidget.plot(self.dataX, self.dataInfected,
                                                  pen=pg.mkPen(color=(255, 0, 0), width=3))
        self.plotHealthy = self.graphWidget.plot(self.dataX, self.dataHealthy, pen=pg.mkPen(color=(0, 255, 0), width=3))
        self.plotDead = self.graphWidget.plot(self.dataX, self.dataDead, pen=pg.mkPen(color=(255, 255, 255), width=3))

    def resumeSimulation(self):
        """this function changes the text of pauseSimButton to Pause"""
        self.pauseSimButton.setText(strings.PAUSE)

    def resetSimulation(self):
        """this function resets the simulation by clearing the scene and the graphWidget and reinitialising the data"""
        self.graphicsView_2.scene().clear()
        self.graphWidget.clear()
        self.dataDead = []
        self.dataHealthy = []
        self.dataInfected = []
        self.dataX = []
        self.plotInfected = self.graphWidget.plot(self.dataX, self.dataInfected, pen=pg.mkPen(color=(255, 0, 0), width=3))
        self.plotHealthy = self.graphWidget.plot(self.dataX, self.dataHealthy, pen=pg.mkPen(color=(0, 255, 0), width=3))
        self.plotDead = self.graphWidget.plot(self.dataX, self.dataDead, pen=pg.mkPen(color=(255, 255, 255), width=3))

    # function visualizes the data from the simulation model in a graphicsview. It uses a new scene for every step.
    def updateParticles(self, particleList, data):
        """this function visualizes the retrieved data from the simulation model in a graphview.
        For every step a new scene is used.

        Args:
            particleList: the list that stores all of the particles that should be drawn
            data: an array of all of the data that holds statistics to the current simulation
        """
        scene = QtWidgets.QGraphicsScene(0, 0, SCENE_DIMENSION, SCENE_DIMENSION)    # scene with 200 x 200 size
        for i in range(0, len(particleList)):
            if(particleList[i].state == strings.HEALTHY):
                pen = QPen(Qt.darkGreen)
                brush = QBrush(Qt.green)
            elif(particleList[i].state == strings.INFECTED):
                pen = QPen(Qt.darkRed)
                brush = QBrush(Qt.red)
            else:   # == strings.DEAD
                pen = QPen(Qt.black)
                brush = QBrush(Qt.darkGray)
            scene.addEllipse(QRectF(particleList[i].x, particleList[i].y, ELLIPSIS_DIMENSION, ELLIPSIS_DIMENSION), pen, brush)
        self.graphicsView_2.setScene(scene)
        self.graphicsView_2.ensureVisible(scene.sceneRect())
        self.graphicsView_2.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
        # self.graphicsView_2.scale(self.graphicsView_2.frameSize() / scene.width(), self.graphicsView_2.frameSize() / scene.height())
        self.i += 1
        if(self.i % 60 == 0):
            self.dataX = data[:,0]
            self.dataHealthy = data[:, 1]
            self.dataInfected = data[:, 2]
            self.dataDead = data[:, 3]
            self.plotInfected.setData(self.dataX, self.dataInfected)
            self.plotHealthy.setData(self.dataX, self.dataHealthy)
            self.plotDead.setData(self.dataX, self.dataDead)