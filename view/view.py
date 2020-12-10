from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPen, QBrush
from PyQt5.QtWidgets import QSlider

from view.mainwindow import Ui_MainWindow


class View(QtWidgets.QMainWindow, Ui_MainWindow):

    startSimulationSignal = QtCore.pyqtSignal()
    pauseSimulationSignal = QtCore.pyqtSignal()
    resetSimulationSignal = QtCore.pyqtSignal()
    speedSimulationSignal = QtCore.pyqtSignal(int)

    def __init__(self):
        super(View, self).__init__()
        self.setupUi(self)
        self.connectSignals()
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(99)
        self.horizontalSlider.setValue(60)
        self.horizontalSlider.setTickInterval(10)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)

    def connectSignals(self):
        self.startSimButton.pressed.connect(self.startSimulationClicked)
        self.pauseSimButton.pressed.connect(self.pauseSimulationClicked)
        self.resetSimButton.pressed.connect(self.resetSimulationClicked)
        self.horizontalSlider.valueChanged.connect(self.speedSimulationChanged)

    def startSimulationClicked(self):
        self.startSimulationSignal.emit()

    def pauseSimulationClicked(self):
        self.pauseSimulationSignal.emit()

    def resetSimulationClicked(self):
        self.resetSimulationSignal.emit()

    def speedSimulationChanged(self):
        self.speedSimulationSignal.emit(self.horizontalSlider.value())

    def startSimulation(self):
        i = 1
        # self.stackedWidget.setCurrentWidget(self.simulatorWidget)

    def pauseSimulation(self):
        i = 1

    def resetSimulation(self):
        self.graphicsView_2.scene().clear()

    def updateParticles(self, particleList):
        print("updateP")
        scene = QtWidgets.QGraphicsScene(0, 0, 200, 200)
        for i in range(0, len(particleList)):
            if(particleList[i].state == "healthy"):
                pen = QPen(Qt.darkGreen)
                brush = QBrush(Qt.green)
            elif(particleList[i].state == "infected"):
                pen = QPen(Qt.darkRed)
                brush = QBrush(Qt.red)
            else:
                pen = QPen(Qt.black)
                brush = QBrush(Qt.darkGray)
            scene.addRect(QRectF(particleList[i].x, particleList[i].y, 5, 5), pen, brush)
        self.graphicsView_2.setScene(scene)
        self.graphicsView_2.ensureVisible(scene.sceneRect())
        self.graphicsView_2.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
        # self.graphicsView_2.scale(self.graphicsView_2.frameSize() / scene.width(), self.graphicsView_2.frameSize() / scene.height())
