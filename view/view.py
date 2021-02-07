from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPen, QBrush
from PyQt5.QtWidgets import QSlider
import numpy as np

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from view.mainwindow import Ui_MainWindow
from view.dialog import Dialog


class View(QtWidgets.QMainWindow, Ui_MainWindow):

    startSimulationSignal = QtCore.pyqtSignal(int, int, int, int, int, int, int)
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
        self.graphWidget.setLabel('left', 'Anzahl der Partikel')
        self.graphWidget.setLabel('bottom', 'Zeit in Sekunden')
        self.plotInfected = self.graphWidget.plot(self.dataX, self.dataInfected, pen=pg.mkPen(color=(255, 0, 0), width=3))
        self.plotHealthy = self.graphWidget.plot(self.dataX, self.dataHealthy, pen=pg.mkPen(color=(0, 255, 0), width=3))
        self.plotDead = self.graphWidget.plot(self.dataX, self.dataDead, pen=pg.mkPen(color=(255, 255, 255), width=3))

    def connectSignals(self):
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
        self.minDaysInfectedSignal.emit(self.spinBox_9.value())

    def maxDaysInfectedChanged(self):
        self.maxDaysInfectedSignal.emit(self.spinBox_10.value())

    def particleRadiusChanged(self):
        self.particleRadiusChangedSignal.emit(self.spinBox_7.value())

    def startSimulationClicked(self):
        self.startSimulationSignal.emit(self.spinBox.value(), self.spinBox_2.value(), self.spinBox_3.value(), self.spinBox_5.value(), self.spinBox_4.value(), self.spinBox_9.value(), self.spinBox_10.value())

    def pauseSimulationClicked(self):
        self.pauseResumeSimulationSignal.emit()

    def resetSimulationClicked(self):
        self.resetSimulationSignal.emit()

    def speedSimulationChanged(self):
        self.speedSimulationSignal.emit(self.horizontalSlider.value())
        self.label_17.setText("x" + str(self.horizontalSlider.value()))

    def infectionRateBoxChanged(self):
        self.infectionRateSignal.emit(self.spinBox_2.value())

    def deathRateBoxChanged(self):
        self.deathRateSignal.emit(self.spinBox_4.value())

    def infectionRadiusBoxChanged(self):
        self.infectionRadiusChangedSignal.emit(self.spinBox_3.value())

    def stayAtHomeClicked(self):
        self.stayAtHomeSignal.emit()

    def export_csvClicked(self):
        self.export_csvSignal.emit()
    
    def ask_granularity(self):
        self.d = Dialog()
        self.d.finishedSignal.connect(self.export_csv)
        self.d.exec_()

    def export_csv(self, granularity):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        print(name[0])
        csvMatrix = np.array([self.dataX, self.dataHealthy, self.dataInfected, self.dataDead]).T
        np.savetxt(name[0], csvMatrix[0::granularity], delimiter=",", fmt='%i', header="Seconds, Healthy, Infected, Dead")

    def showExportAlert(self, simulation):
        dlg = QtWidgets.QDialog(self)
        dlg.setWindowTitle("Fehler beim Export!")
        label = QtWidgets.QLabel(dlg)
        if simulation != None:
            label.setText("Export bei laufender Simulation nicht möglich!")
        else:
            label.setText("Export bei noch nicht gestarteter Simulation nicht möglich!")
        label.adjustSize()
        label.move(100, 60)
        dlg.exec_()

    def showAlert(self, message):
        dlg = QtWidgets.QDialog(self)
        dlg.setWindowTitle("Fehler beim Export!")
        label = QtWidgets.QLabel(dlg)
        label.setText(message)
        label.adjustSize()
        label.move(100, 60)
        dlg.exec_()

    def pauseSimulation(self):
        self.pauseSimButton.setText("Weiter")

    def startSimulation(self):
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
        self.pauseSimButton.setText("Pause")

    # resets by clearing the scene
    def resetSimulation(self):
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
            scene.addEllipse(QRectF(particleList[i].x, particleList[i].y, 5, 5), pen, brush)
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