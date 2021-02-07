from PyQt5 import QtCore

from view.view import View
from view.dialog import Dialog
from model.simulation import Simulation

import resources.strings as strings

FPS = 60

class Presenter(QtCore.QObject):
    """The presenter acts upon the model and the view. It retrieves data from the model (simulation), and formats it to display it in the view."""
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
        """this function is used to process the steps as long as the simulation is running.
        It performs the steps and it retrieves the data from the model and updates the data in the view"""
        if self.isSimulationRunning:
            self.simulation.performStep()
            self.ui.updateParticles(self.simulation.getParticles(), self.simulation.getData())

    def startSimulation(self, xBorder, yBorder, countParticles, infectionRate, infectionRadius, initiallyInfected, deathRate, minDaysInfected, maxDaysInfected):
        """this function is used to initiate a simulation. It starts the simulation with the given arguments
        Args:
            xBorder: the maximum x-coordinate particles are allowed to move to the right
            yBorder: the maximum y-coordinate particles are allowed to move down
            countParticles: the number of particles the simulation should hold (default: 100)
            infectionRate: the initially set infection rate which with particles can infect each other
            infectionRadius: the initially set infection radius, which is used to detect collisions of the particles
            initiallyInfected: the initial number of particles that are infected by the start of the simulation
            deathRate: the initially set death rate within the simulation
            minDaysInfected: the minimum of days particles have to be infected
            maxDaysInfected the maximum of day particles can be infected up to
        """
        self.isSimulationRunning = True
        self.simulation = Simulation(xBorder, yBorder, countParticles, infectionRate, infectionRadius, initiallyInfected, deathRate, minDaysInfected, maxDaysInfected)
        self.ui.startSimulation()
        self.ui.resumeSimulation()

    def pauseResumeSimulation(self):
        """this function is used to pause or to resume the current simulation"""
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

    def resetSimulation(self):
        """this function is used to stop and reset the current simulation"""
        self.isSimulationRunning = False
        self.isSimulationPaused = False
        self.simulation = None
        self.ui.resetSimulation()
        self.ui.resumeSimulation()

    def speedSimulation(self, value):
        """this function is used to change the current speed of the simulation
        Args:
            value: the new value by which factor to normal (1) the simulation has to be speed up
        """
        self.timer.setInterval(int((1/value * 1000) / FPS))

    def changeInfectionRate(self, infectionRate):
        """this function changes the infection rate of the current simulation
        Args:
            infectionRate: the new infection rate
        """
        if self.isSimulationRunning:
            self.simulation.setInfectionRate(infectionRate)

    def changeDeathRate(self, deathRate):
        """this function changes the death rate of the current simulation
        Args:
            deathRate: the new death rate
        """
        if self.isSimulationRunning:
            self.simulation.setDeathRate(deathRate)

    # changes the particles infectionRadius
    def changeinfectionRadius(self, infectionRadius):
        """this function changes the infection radius of the current simulation
        Args:
            infectionRadius: the new infection radius
        """
        if(self.simulation != None):
            self.simulation.setinfectionRadius(infectionRadius)

    def export_csv(self):
        """this function checks whether the simulation is running.
        If not it is allowing the view to show its exportDialog.
        """
        if(self.isSimulationPaused == True):
            self.ui.ask_granularity()
        else:
            if self.simulation:
                self.ui.showAlert("Export bei laufender Simulation nicht möglich!")
            else:
                self.ui.showAlert("Export bei noch nicht gestarteter Simulation nicht möglich!")

    def changeStayAtHome(self):
        """this fucntion changes the current behaviour of simulating people are staying at home"""
        if self.isSimulationRunning:
            self.simulation.changePeopleStayAtHome()

    def changeParticleRadius(self, radius):
        """this function changes the particles radii in the current simulation"""
        if self.simulation:
            self.simulation.changeParticleRadius(radius)

    def changeMinDaysInfected(self, minDaysInfected):
        """this function changes the minimum days particles have to be infected in the current simulation
        Args:
            minDaysInfected: the minimum days particles have to be infected
        """
        if self.simulation:
            if self.simulation.maxDaysInfected >= minDaysInfected:
                self.simulation.setMinDaysInfected(minDaysInfected)
            else:
                self.ui.showAlert(strings.MIN_UNDER_MAX_ALERT)

    def changeMaxDaysInfected(self, maxDaysInfected):
        """this function changes the maximum days particles are able to be infected in the current simulation
        Args:
            maxDaysInfected: the maximum days particles are able to be infected
        """
        if self.simulation:
            if self.simulation.minDaysInfected <= maxDaysInfected:
                self.simulation.setMaxDaysInfected(maxDaysInfected)
            else:
                self.ui.showAlert(strings.MAX_UNDER_MIN_ALERT)

    def _connectUIElements(self) -> None:
        """this function is used to connect all of the signals between the view and the presenter"""
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