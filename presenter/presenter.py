from PyQt5 import QtCore

from view.view import View
from view.dialog import Dialog
from model.simulation import Simulation

FPS = 60

class Presenter(QtCore.QObject):
    def __init__(self):
        super(Presenter, self).__init__()
        # create main window
        self.ui = View()
        self.ui2 = Dialog()
        self.simulation = None
        self.isSimulationRunning = False
        self.isSimulationPaused = False

        # create timer that will call the mainLoop every 1000/FPS milliseconds
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.mainLoop)
        self.timer.start(int(1000 / FPS))
        self.framecounter = 0

        self._connectUIElements()

    def mainLoop(self):
        if self.isSimulationRunning:
            self.simulation.performStep()
            self.ui.updateParticles(self.simulation.getParticles(), self.simulation.getData())
            # self.ui.updateData(self.simulation.getData())

    # starts the simulation with the given arguments
    def startSimulation(self, countParticles, infectionRate, infectionRadius, initiallyInfected, deathRate, minDaysInfected, maxDaysInfected):
        self.isSimulationRunning = True
        self.simulation = Simulation(countParticles, infectionRate, infectionRadius, initiallyInfected, deathRate, minDaysInfected, maxDaysInfected)
        self.ui.startSimulation()
        self.ui.resumeSimulation()

    # pauses or resumes the simulation
    def pauseResumeSimulation(self):
        if self.simulation != None:
            if(self.isSimulationPaused == False):
                self.isSimulationRunning = False
                self.isSimulationPaused = True
                self.ui.pauseSimulation()
            else:
                self.isSimulationRunning = True
                self.isSimulationPaused = False
                self.ui.resumeSimulation()
        else:
            self.ui.resumeSimulation()

    # resets the simulation
    def resetSimulation(self):
        self.isSimulationRunning = False
        self.isSimulationPaused = False
        self.simulation = None
        self.ui.resetSimulation()
        self.ui.resumeSimulation()

    # changes the FPS of the simulation
    def speedSimulation(self, value):
        self.timer.setInterval(int((1/value * 1000) / FPS))

    # changes the infection rate
    def changeInfectionRate(self, infectionRate):
        if self.isSimulationRunning:
            self.simulation.setInfectionRate(infectionRate)

        # changes the death rate
    def changeDeathRate(self, deathRate):
        if self.isSimulationRunning:
            self.simulation.setDeathRate(deathRate)

    # changes the particles infectionRadius
    def changeinfectionRadius(self, infectionRadius):
        if(self.simulation != None):
            self.simulation.setinfectionRadius(infectionRadius)

    def export_csv(self):
        if(self.isSimulationPaused == True):
            self.ui.ask_granularity()
        else:
            self.ui.showExportAlert(self.simulation)

    def changeStayAtHome(self):
        if self.isSimulationRunning:
            self.simulation.changePeopleStayAtHome()

    def changeParticleRadius(self, radius):
        if self.simulation:
            self.simulation.changeParticleRadius(radius)

    def changeMinDaysInfected(self, minDaysInfected):
        if self.simulation:
            if self.simulation.maxDaysInfected >= minDaysInfected:
                self.simulation.setMinDaysInfected(minDaysInfected)
            else:
                self.ui.showAlert("Die minimale Infektionsdauer kann nicht über der maximalen Infektionsdauer liegen!")

    def changeMaxDaysInfected(self, maxDaysInfected):
        if self.simulation:
            if self.simulation.minDaysInfected <= maxDaysInfected:
                self.simulation.setMaxDaysInfected(maxDaysInfected)
            else:
                self.ui.showAlert("Die maximale Infektionsdauer kann nicht unter der minimalen Infektionsdauer liegen!")

    def _connectUIElements(self) -> None:
        # elements of the main window
        self.ui.startSimulationSignal.connect(self.startSimulation)
        self.ui.pauseResumeSimulationSignal.connect(self.pauseResumeSimulation)
        self.ui.resetSimulationSignal.connect(self.resetSimulation)
        self.ui.speedSimulationSignal.connect(self.speedSimulation)
        self.ui.infectionRateSignal.connect(self.changeInfectionRate)
        self.ui.deathRateSignal.connect(self.changeDeathRate)
        self.ui.infectionRadiusChangedSignal.connect(self.changeinfectionRadius)
        self.ui.export_csvSignal.connect(self.export_csv)
        self.ui.stayAtHomeSignal.connect(self.changeStayAtHome)
        self.ui.particleRadiusChangedSignal.connect(self.changeParticleRadius)
        self.ui.minDaysInfectedSignal.connect(self.changeMinDaysInfected)
        self.ui.maxDaysInfectedSignal.connect(self.changeMaxDaysInfected)