### SEIRD_Model_Simulation
This repository contains a Python simulation of the SEIRD (Susceptible, Exposed, Infected, Recovered, Dead) epidemic model. Using the Python turtle module for visualization, the simulation models the spread and control of an infectious disease within a population over time.
Files

    agent.py: Defines the Agent class to represent individuals in the population. Agents have states representing their disease status (Susceptible, Exposed, Infected, Recovered, Dead) and behaviors such as movement, infection transmission, and collision avoidance.
    box.py: Implements the Box class, used for creating bounded areas such as hospitals and cemeteries in the simulation space.
    modeler.py: Contains the main simulation loop that initializes the population, updates agents' states, and triggers their interactions.
    utils.py: Provides utility functions for displaying the count of agents in each state and for plotting the progression of the epidemic using matplotlib.
    SIR.png: An example output graph showing the dynamics of the epidemic over time, with the number of susceptible, exposed, infected, recovered, and dead individuals.

Features

    Real-time simulation of agent interactions and disease spread.
    Customizable parameters for population size, initial number of infected individuals, and the size of specialized areas like hospitals.
    A graph output showing the time evolution of the disease states within the population.
  
