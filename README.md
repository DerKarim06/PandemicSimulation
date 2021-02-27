# Pandemic Simulation

This Pandemic Simulation is a Python application for simulating pandemics with different parameters. (WARNING: This simulation can only be used in a non scientific environment and can not be referenced as it not representing real pandemic circumstances.)

## Installation

Clone this repo, install the dependencies with pip from the requirement.txt and start the application from main.py.

```bash
git clone https://btn7k8.inf.uni-bayreuth.de/gitlab/praktikum2021/ai-1/karim.git
pip install requirements.txt
python main.py
```

# Usage

## Standard simulation

This can be used to simulate a pandemic with the given parameters. It is possible to see the progress live on the left with particles moving around and on the right with the statistical data being drawn on a graph.

![](standardSim.png)

There are different parameters that can be configured:

**General parameters:**

- Number of particles (self explanatory)
- Number of initial infected particles (self explanatory)
- Simulation speed (self explanatory)

**Infection related parameters:**

- Infection rate (probability with which particles can infect each other)
- Infection radius (size of the radius in which the probability of infection is activated)
- Death rate (probability with which particles are dying after their infection)
- Minimum days of Infection (self explanatory)
- Maximum days of Infection (self explanatory)
- Immune percentage (percentage of particles being immune after their infection)
- Minimum days of being Immune (self explanatory)
- Maximum days of being Immune (self explanatory)

**Vaccination related parameters:**

- Activate Vaccine (vaccination means endlessly being immune)
- Date of Vaccine (After this date the vaccination progress begins)
- Speed of Vaccination (Number of particles being vaccinated per day)
- Activate that healthy particles are vaccinated before immune ones (self explanatory)

**Movement related parameters:**

- People staying at home (particles are gathering together at home, some particles are nevertheless changing their places until everyone is at their place)
- Distance radius (the amount of distance particles hold to each other)
- Quarantine percentage (percentage of infected particles that quarantine and therefore cannot infect others)

## Running multiple simulations

As one simulation has a lot of probability variables in its process, it is safer to run multiple simulations to see an average in the pandemic progress across all of the simulations. With this option you can run multiple simulations and the results are displayed on different graphs. (WARNING: The processing can take a lot of time as there are multiple simulations processed. I.e. the standard configuration takes about 30 seconds to be processed.)

![](multipleSim.png)

There are different parameters that can be configured:

**General parameters:**

- Number of simultaneously simulations (self explanatory)
- Duration of the simulations (self explanatory)
- Number of particles (self explanatory)
- Number of initial infected particles (self explanatory)

**Infection related parameters:**

- Infection rate (probability with which particles can infect each other)
- Infection radius (size of the radius in which the probability of infection is activated)
- Death rate (probability with which particles are dying after their infection)
- Minimum days of Infection (self explanatory)
- Maximum days of Infection (self explanatory)
- Immune percentage (percentage of particles being immune after their infection)
- Minimum days of being Immune (self explanatory)
- Maximum days of being Immune (self explanatory)

**Vaccination related parameters:**

- Activate Vaccine (vaccination means endlessly being immune)
- Date of Vaccine (After this date the vaccination progress begins)
- Speed of Vaccination (Number of particles being vaccinated per day)
- Activate that healthy particles are vaccinated before immune ones (self explanatory)

**Movement related parameters:**

- Distance radius (the amount of distance particles hold to each other)
- Quarantine percentage (percentage of infected particles that quarantine and therefore cannot infect others)

## Running a SIRD-model calculation

The Susceptible-Infectious-Recovered-Deceased-Model differentiates between Recovered (meaning specifically individuals having survived the disease and now immune) and Deceased. See [The SIRD model](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology#The_SIRD_model) for further information

This dialog can be used to calculate a SIRD-model with the given parameters. This option can be used i.e. to check how the pandemic would turn out with a realistic mathematical-epidemiological model calculation.


![](SIRD.png)

There are different parameters that can be configured:

- population (self explanatory)
- Number of initial infected people (self explanatory)
- infection rate(self explanatory)
- rate of recovery (rate of becoming recovered after infection)
- death rate (self explanatory)
- time steps (given in days and will be displayed in weeks)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

