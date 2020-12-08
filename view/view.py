from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt

from view.mainwindow import Ui_MainWindow


class View(QtWidgets.QMainWindow, Ui_MainWindow):

    startSimulationSignal = QtCore.pyqtSignal()
    pauseSimulationSignal = QtCore.pyqtSignal()
    resetSimulationSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(View, self).__init__()
        self.setupUi(self)

        self.connectSignals()

    def connectSignals(self):
        self.startSimButton.pressed.connect(self.startSimulationClicked)
        self.pauseSimButton.pressed.connect(self.pauseSimulationClicked)
        self.resetSimButton.pressed.connect(self.resetSimulationClicked)

    def startSimulationClicked(self):
        self.startSimulationSignal.emit()

    def pauseSimulationClicked(self):
        self.pauseSimulationSignal.emit()

    def resetSimulationClicked(self):
        self.resetSimulationSignal.emit()

    def startSimulation(self):
        i = 1
        # self.stackedWidget.setCurrentWidget(self.simulatorWidget)

    def pauseSimulation(self):
        i = 1

    def resetSimulation(self):
        self.graphicsView_2.scene().hide()

    def updateScene(self, scene):
        self.graphicsView_2.setScene(scene)
        self.graphicsView_2.ensureVisible(scene.sceneRect())
        self.graphicsView_2.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
        # self.graphicsView_2.scale(self.graphicsView_2.frameSize() / scene.width(), self.graphicsView_2.frameSize() / scene.height())
