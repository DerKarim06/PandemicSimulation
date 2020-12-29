from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPen, QBrush
from PyQt5.QtWidgets import QSlider
import numpy as np

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from view.mainwindow import Ui_MainWindow


class View(QtWidgets.QMainWindow, Ui_MainWindow):

    startSimulationSignal = QtCore.pyqtSignal(int, int)
    pauseSimulationSignal = QtCore.pyqtSignal()
    resetSimulationSignal = QtCore.pyqtSignal()
    speedSimulationSignal = QtCore.pyqtSignal(int)
    infectionRateSignal = QtCore.pyqtSignal(int)
    radiusChangedSignal = QtCore.pyqtSignal(int)
    export_csvSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(View, self).__init__()
        self.setupUi(self)
        self.connectSignals()
        # FPS slider
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(99)
        self.horizontalSlider.setValue(60)
        self.horizontalSlider.setTickInterval(10)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        # particle count spinbox
        self.spinBox.setMaximum(1000)
        self.spinBox.setValue(100)
        #infection rate spinbox
        self.spinBox_2.setValue(5)
        # radius spinbox
        self.spinBox_3.setValue(3)
        self.i = 0
        self.j = 0

        self.dataX = []
        self.dataInfected = []
        self.dataHealthy = []
        self.dataDead = []

        self.graphWidget.setBackground('w')
        self.graphWidget.setLabel('left', 'Anzahl der Partikel')
        self.graphWidget.setLabel('bottom', 'Zeit in Sekunden')
        self.plotInfected = self.graphWidget.plot(self.dataX, self.dataInfected, pen=pg.mkPen(color=(255, 0, 0), width=6))
        self.plotHealthy = self.graphWidget.plot(self.dataX, self.dataHealthy, pen=pg.mkPen(color=(0, 255, 0), width=6))
        self.plotDead = self.graphWidget.plot(self.dataX, self.dataDead, pen=pg.mkPen(color=(0, 0, 0), width=6))

    def connectSignals(self):
        self.startSimButton.pressed.connect(self.startSimulationClicked)
        self.pauseSimButton.pressed.connect(self.pauseSimulationClicked)
        self.resetSimButton.pressed.connect(self.resetSimulationClicked)
        self.horizontalSlider.valueChanged.connect(self.speedSimulationChanged)
        self.spinBox_2.valueChanged.connect(self.infectionRateBoxChanged)
        self.spinBox_3.valueChanged.connect(self.radiusBoxChanged)
        self.actionExport_CSV.triggered.connect(self.export_csvClicked)

    def startSimulationClicked(self):
        self.startSimulationSignal.emit(self.spinBox.value(), self.spinBox_3.value())

    def pauseSimulationClicked(self):
        self.pauseSimulationSignal.emit()

    def resetSimulationClicked(self):
        self.resetSimulationSignal.emit()

    def speedSimulationChanged(self):
        self.speedSimulationSignal.emit(self.horizontalSlider.value())

    def infectionRateBoxChanged(self):
        self.infectionRateSignal.emit(self.spinBox_2.value())

    def radiusBoxChanged(self):
        self.radiusChangedSignal.emit(self.spinBox_3.value())

    def export_csvClicked(self):
        self.export_csvSignal.emit()
    
    def export_csv(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        print(name[0])
        csvMatrix = np.array([self.dataX, self.dataHealthy, self.dataInfected, self.dataDead]).T
        np.savetxt(name[0] + ".csv", csvMatrix, delimiter=",", fmt='%i', header="Seconds, Healthy, Infected, Dead")

    #TODO: implement starting from paused state
    def pauseSimulation(self):
        i = 1

    # resets by clearing the scene
    def resetSimulation(self):
        self.graphicsView_2.scene().clear()
        self.graphWidget.clear()
        self.dataDead.clear()
        self.dataHealthy.clear()
        self.dataInfected.clear()
        self.dataX.clear()
        self.plotInfected = self.graphWidget.plot(self.dataX, self.dataInfected, pen=pg.mkPen(color=(255, 0, 0), width=6))
        self.plotHealthy = self.graphWidget.plot(self.dataX, self.dataHealthy, pen=pg.mkPen(color=(0, 255, 0), width=6))
        self.plotDead = self.graphWidget.plot(self.dataX, self.dataDead, pen=pg.mkPen(color=(0, 0, 0), width=6))

    # function visualizes the data from the simulation model in a graphicsview. It uses a new scene for every step.
    def updateParticles(self, particleList):
        scene = QtWidgets.QGraphicsScene(0, 0, 200, 200)    # scene with 200 x 200 size
        for i in range(0, len(particleList)):
            if(particleList[i].state == "healthy"):
                pen = QPen(Qt.darkGreen)
                brush = QBrush(Qt.green)
            elif(particleList[i].state == "infected"):
                pen = QPen(Qt.darkRed)
                brush = QBrush(Qt.red)
            else:   # only for later use (dead particles)
                pen = QPen(Qt.black)
                brush = QBrush(Qt.darkGray)
            scene.addRect(QRectF(particleList[i].x, particleList[i].y, 5, 5), pen, brush)
        self.graphicsView_2.setScene(scene)
        self.graphicsView_2.ensureVisible(scene.sceneRect())
        self.graphicsView_2.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
        # self.graphicsView_2.scale(self.graphicsView_2.frameSize() / scene.width(), self.graphicsView_2.frameSize() / scene.height())
        self.i += 1
        if(self.i % 60 == 0):
            j = 0
            k = 0
            l = 0
            for i in range(0, len(particleList)):
                if(particleList[i].state == 'dead'):
                    l += 1
                if (particleList[i].state == "infected"):
                    j += 1
                if(particleList[i].state == "healthy"):
                    k += 1
            self.dataX.append(int(self.i/60))
            self.dataInfected.append(j)
            self.dataHealthy.append(k)
            self.dataDead.append(l)
            self.plotInfected.setData(self.dataX, self.dataInfected)
            self.plotHealthy.setData(self.dataX, self.dataHealthy)
            self.plotDead.setData(self.dataX, self.dataDead)