from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPen, QBrush
from PyQt5.QtWidgets import QSlider

from view.mainwindow import Ui_MainWindow


class View(QtWidgets.QMainWindow, Ui_MainWindow):

    startSimulationSignal = QtCore.pyqtSignal(int, int)
    pauseSimulationSignal = QtCore.pyqtSignal()
    resetSimulationSignal = QtCore.pyqtSignal()
    speedSimulationSignal = QtCore.pyqtSignal(int)
    radiusChangedSignal = QtCore.pyqtSignal(int)

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
        # radius spinbox
        self.spinBox_3.setValue(3)

    def connectSignals(self):
        self.startSimButton.pressed.connect(self.startSimulationClicked)
        self.pauseSimButton.pressed.connect(self.pauseSimulationClicked)
        self.resetSimButton.pressed.connect(self.resetSimulationClicked)
        self.horizontalSlider.valueChanged.connect(self.speedSimulationChanged)
        self.spinBox_3.valueChanged.connect(self.radiusBoxChanged)

    def startSimulationClicked(self):
        self.startSimulationSignal.emit(self.spinBox.value(), self.spinBox_3.value())

    def pauseSimulationClicked(self):
        self.pauseSimulationSignal.emit()

    def resetSimulationClicked(self):
        self.resetSimulationSignal.emit()

    def speedSimulationChanged(self):
        self.speedSimulationSignal.emit(self.horizontalSlider.value())

    def radiusBoxChanged(self):
        self.radiusChangedSignal.emit(self.spinBox_3.value())

    #TODO: implement starting from paused state
    def pauseSimulation(self):
        i = 1

    # resets by clearing the scene
    def resetSimulation(self):
        self.graphicsView_2.scene().clear()

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
