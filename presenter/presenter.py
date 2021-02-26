from PyQt5 import QtCore

from view.view import View
from model.sird import SIRD
from model.simulation import Simulation

import resources.constants as constants

FPS = 60


class Presenter(QtCore.QObject):
    """The presenter acts upon the model and the view. It retrieves data from the model (simulation), and formats it to display it in the view."""

    def __init__(self):
        super(Presenter, self).__init__()
        # create main window
        self.ui = View()
        self.dialog = None
        self.simulation = None
        self.isSimulationRunning = False
        self.isSimulationPaused = False

        # create timer that will call the mainLoop every 1000/FPS milliseconds
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.mainLoop)
        self.timer.start((1000 / FPS))
        self.framecounter = 0

        self._connectUIElements()

    def mainLoop(self):
        """this function is used to process the steps as long as the simulation is running.
        It performs the steps and it retrieves the data from the model and updates the data in the view"""
        if self.isSimulationRunning:
            self.simulation.performStep()
            self.ui.updateParticles(self.simulation.getParticles(), self.simulation.getData())

    def startSimulation(self, xBorder, yBorder, percentageImmune, minImmuneDuration, maxImmuneDuration, countParticles,
                        infectionRate, infectionRadius, initiallyInfected, deathRate, minDaysInfected, maxDaysInfected,
                        quarantinePercentage, vaccinationActivated, vaccinationBegin, vaccinationSpeed,
                        vaccinateHealthyFirst):
        """this function is used to initiate a simulation. It starts the simulation with the given arguments
        Args:
            xBorder: the maximum x-coordinate particles are allowed to move to the right
            yBorder: the maximum y-coordinate particles are allowed to move down
            percentageImmune: the percentage of being immune after recovery
            minImmuneDuration: the minimum duration of being immune
            maxImmuneDuration: the maximum duration of being immune
            countParticles: the number of particles the simulation should hold
            infectionRate: the initially set infection rate which with particles can infect each other
            infectionRadius: the initially set infection radius, which is used to detect collisions of the particles
            initiallyInfected: the initial number of particles that are infected by the start of the simulation
            deathRate: the initially set death rate within the simulation
            minDaysInfected: the minimum of days particles have to be infected
            maxDaysInfected the maximum of days particles can be infected
            quarantinePercentage: the percentage of particles being in quarantine when infected
            vaccinationActivated: whether vaccination is activated in the current simulation
            vaccinationBegin: the start of vaccination in days
            vaccinationSpeed: the count of particles being able to be vaccinated in one day
            vaccinateHealthyFirst: whether the first one getting vaccinated are the healthy ones
        """
        if countParticles < initiallyInfected:
            self.ui.showAlert(constants.PARTICLES_ALERT)
        elif minDaysInfected > maxDaysInfected:
            self.ui.showAlert(constants.INFECTION_MIN_OVER_MAX_ALERT)
        elif minImmuneDuration > maxImmuneDuration:
            self.ui.showAlert(constants.IMMUNE_MIN_OVER_MAX_ALERT)
        else:
            if self.isSimulationPaused:
                self.resetSimulation()
            self.isSimulationRunning = True
            self.simulation = Simulation(xBorder, yBorder, percentageImmune, minImmuneDuration, maxImmuneDuration,
                                         countParticles, infectionRate, infectionRadius, initiallyInfected, deathRate,
                                         minDaysInfected, maxDaysInfected, quarantinePercentage, vaccinationActivated,
                                         vaccinationBegin, vaccinationSpeed, vaccinateHealthyFirst)
            self.ui.startSimulation()
            self.ui.resumeSimulation()

    def pauseResumeSimulation(self):
        """this function is used to pause or to resume the current simulation"""
        if self.simulation != None:
            if (self.isSimulationPaused == False):
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
        self.timer.setInterval((1 / value * 1000) / FPS)

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
        if (self.simulation != None):
            self.simulation.setInfectionRadius(infectionRadius)

    def export_csv(self):
        """this function checks whether the simulation is running or has never started.
        If not it is allowing the view to show its exportDialog.
        """
        if (self.isSimulationPaused == True):
            self.ui.ask_granularity()
        else:
            if self.simulation:
                self.ui.showAlert(constants.EXPORT_CSV_SIMULATION_RUNNING_ALERT)
            else:
                self.ui.showAlert(constants.EXPORT_CSV_NO_SIMULATION_ALERT)

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
                self.ui.showAlert(constants.INFECTION_MIN_OVER_MAX_ALERT)

    def changeMaxDaysInfected(self, maxDaysInfected):
        """this function changes the maximum days particles are able to be infected in the current simulation
        Args:
            maxDaysInfected: the maximum days particles are able to be infected
        """
        if self.simulation:
            if self.simulation.minDaysInfected <= maxDaysInfected:
                self.simulation.setMaxDaysInfected(maxDaysInfected)
            else:
                self.ui.showAlert(constants.INFECTION_MAX_UNDER_MIN_ALERT)

    def changePercentageImmune(self, percentage):
        """this function changes the percentage of particles to be immune in the current simulation
        Args:
            percentage: the new percentage of particles being immune afterwards
        """
        self.simulation.setPercentageImmune(percentage)

    def changeMaxImmuneDuration(self, duration):
        """this function changes the maximum duration particles are allow to be immune in the current simulation
        Args:
            duration: the new maximum duration to be immune
        """
        if self.simulation:
            if self.simulation.minImmuneDuration <= duration:
                self.simulation.setMaxImmuneDuration(duration)
            else:
                self.ui.showAlert(constants.IMMUNE_MAX_UNDER_MIN_ALERT)

    def changeMinImmuneDuration(self, duration):
        """this function changes the minimum duration particles are allow to be immune in the current simulation
        Args:
            duration: the new minimum duration to be immune
        """
        if self.simulation:
            if self.simulation.maxImmuneDuration >= duration:
                self.simulation.setMinImmuneDuration(duration)
            else:
                self.ui.showAlert(constants.IMMUNE_MIN_OVER_MAX_ALERT)

    def changeQuarantinePercentage(self, percentage):
        """this function changes the percentage of particles that are in quarantine while being infected
        Args:
            percentage: the new percentage of quarantining particles
        """
        if self.simulation:
            self.simulation.setQuarantinePercentage(percentage)

    def startMultipleSimulations(self, simCount, simDuration, countParticles, initiallyInfected, infectionRate,
                                 infectionRadius, deathRate, minDaysInfected, maxDaysInfected, percentageImmune,
                                 minImmuneDuration, maxImmuneDuration, distanceRadius, quarantinePercentage,
                                 vaccinationActivated, vaccinationDate, vaccinationSpeed, vaccinateHealthyFirst, dialog,
                                 xBorder=0, yBorder=195):
        """this function is used to initiate multiple simulations. It starts all of the simulations with the given
        arguments
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
            dialog: the dialog for the presenter from where the call came
            xBorder: the maximum x-coordinate particles are allowed to move to the right (default: 0)
            yBorder: the maximum y-coordinate particles are allowed to move down (default: 195)
        """
        self.simulations = []
        self.dialog = dialog
        for i in range(0, simCount):
            s = Simulation(xBorder, yBorder, percentageImmune, minImmuneDuration, maxImmuneDuration, countParticles,
                           infectionRate, infectionRadius, initiallyInfected, deathRate, minDaysInfected,
                           maxDaysInfected, quarantinePercentage, vaccinationActivated, vaccinationDate,
                           vaccinationSpeed, vaccinateHealthyFirst)
            s.changeParticleRadius(distanceRadius)
            self.simulations.append(s)
        for i in range(0, simDuration * FPS):
            data = []
            for j in range(0, len(self.simulations)):
                self.simulations[j].performStep()
                data.append(self.simulations[j].getData())
            self.dialog.updateData(data)

    def startSIRD(self, population, initiallyInfected, infectionRate, healthyRate, deathRate, days, dialog):
        """this function start the sird model calculation and sends it to the dialog which started the process
        Args:
            population: the amount of particles for the simulation
            initiallyInfected: the amount of initially infected particles from the population
            infectionRate: the infection rate
            healthyRate: the rate of being immune
            deathRate: the rate of being dead after infection
            days: the amount of days the simulation should process
            dialog: the dialog that initiated the calculation
        """
        self.dialog = dialog
        if initiallyInfected > population:
            self.dialog.showAlert(constants.PARTICLES_ALERT)
        else:
            sird = SIRD(population, initiallyInfected, infectionRate, healthyRate, deathRate, days)
            dialog.updateData(sird.getData())

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
        self.ui.percentageImmuneSignal.connect(self.changePercentageImmune)
        self.ui.maxImmuneDurationSignal.connect(self.changeMaxImmuneDuration)
        self.ui.minImmuneDurationSignal.connect(self.changeMinImmuneDuration)
        self.ui.quarantinePercentageSignal.connect(self.changeQuarantinePercentage)
        self.ui.multipleSimulationSignal.connect(self.startMultipleSimulations)
        self.ui.sirdSignal.connect(self.startSIRD)
