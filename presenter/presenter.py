from PyQt5 import QtCore

from view.view import View
from model.simulation import Simulation

FPS = 60

class Presenter(QtCore.QObject):
    def __init__(self):
        super(Presenter, self).__init__()
        # create main window
        self.ui = View()
        self.simulation = None
        self.isSimulationRunning = False

        # create timer that will call the mainLoop every 1000/FPS milliseconds
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.mainLoop)
        self.timer.start(int(1000 / FPS))
        self.framecounter = 0

        self._connectUIElements()

    def mainLoop(self):
        if self.isSimulationRunning:
            self.simulation.performStep()
            self.ui.updateParticles(self.simulation.getParticles())
            # self.ui.updateData(self.simulation.getData())

    # starts the simulation with the given arguments
    def startSimulation(self, countParticles, radius):
        self.isSimulationRunning = True
        self.simulation = Simulation(countParticles, radius)

    # pauses the simulation
    def pauseSimulation(self):
        self.isSimulationRunning = False
        self.ui.pauseSimulation()

    # resets the simulation
    def resetSimulation(self):
        self.isSimulationRunning = False
        self.simulation = None
        self.ui.resetSimulation()

    # changes the FPS of the simulation
    def speedSimulation(self, value):
        self.timer.disconnect()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.mainLoop)
        self.timer.start(int(1000 / value))

    # changes the infection rate
    def changeInfectionRate(self, infectionRate):
        self.simulation.setInfectionRate(infectionRate)

    # changes the particles radius
    def changeRadius(self, radius):
        if(self.simulation != None):
            self.simulation.setRadius(radius)

    def export_csv(self):
        if(self.isSimulationRunning == False):
            self.ui.export_csv()

    def _connectUIElements(self) -> None:
        # elements of the main window
        self.ui.startSimulationSignal.connect(self.startSimulation)
        self.ui.pauseSimulationSignal.connect(self.pauseSimulation)
        self.ui.resetSimulationSignal.connect(self.resetSimulation)
        self.ui.speedSimulationSignal.connect(self.speedSimulation)
        self.ui.infectionRateSignal.connect(self.changeInfectionRate)
        self.ui.radiusChangedSignal.connect(self.changeRadius)
        self.ui.export_csvSignal.connect(self.export_csv)