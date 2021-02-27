import numpy as np
from scipy import integrate


class SIRD:
    """this class represents the simulation via the SIRD-model"""

    def __init__(self, population, initiallyInfected, infectionRate, healthyRate, deathRate, days):
        """
        this is the constructor of the class. the simulations processes the steps in weeks

        Args:
            population: the amount of particles for the simulation
            initiallyInfected: the amount of initially infected particles from the population
            infectionRate: the infection rate
            healthyRate: the rate of being immune
            deathRate: the rate of being dead after infection
            days: the amount of days the simulation should process
        """
        self.population = population
        self.initiallyInfected = initiallyInfected
        self.infectionRate = infectionRate
        self.healthyRate = healthyRate
        self.deathRate = deathRate
        self.days = days

        self.S0 = 1 - (self.initiallyInfected / self.population)
        self.I0 = self.initiallyInfected / self.population
        self.R0 = 0
        self.D0 = 0

        conc0 = [self.S0, self.I0, self.R0, self.D0]

        # steps are weeks
        dt = 1 / 7

        self.t = np.arange(days) * dt
        self.r = integrate.odeint(self.performStep, conc0, self.t)

        self.data = [self.t, self.r]

    def performStep(self, conc, t):
        """this function processes one step of the SIRD-model

        Args:
            conc: storage of the S, I, R and D data
            t: the current step

        Returns:
            the new delta S, I, R and D for the step t (as tupel)
            """
        S = conc[0]
        I = conc[1]
        R = conc[2]
        D = conc[3]

        dS = - self.infectionRate * S * I
        dI = self.infectionRate * S * I - self.healthyRate * I - self.deathRate * I
        dR = self.healthyRate * I
        dD = self.deathRate * I

        return (dS, dI, dR, dD)

    def getData(self):
        """this function returns the data the model holds

        Returns:
            the stored data from the class
        """
        return self.data
