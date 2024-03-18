### SEIRD_Model_Simulation
Welcome to the SEIRD Model Simulation repository! The simulation is a representation of an enclosed ecosystem where individuals, represented by agents, interact with each other within defined spaces such as the general population area, a hospital, and a cemetery. These interactions can lead to the spread of an infectious disease, following a modified SEIRD model which includes an exposed (latent infection) state.

## Project Overview
The SEIRD model is a compartmental model used in epidemiology to simulate the progression and control of infectious diseases. In this simulation:
- **Susceptible (S)**: Individuals who can contract the disease.
- **Exposed (E)**: Individuals who have been exposed to the disease but are not yet infectious.
- **Infected (I)**: Individuals who have been infected and can spread the disease to others.
- **Recovered (R)**: Individuals who have recovered from the disease and are no longer infectious.
- **Dead (D)**: Individuals who have died from the disease.

## Simulation Flow

At each timestep, the following occurs:

   1. Agents move within the simulation box, with infected individuals heading towards the hospital and dead agents being relocated to the cemetery.
   2. Interactions between agents are computed to determine the spread of infection based on proximity and collision detection.
   3. The states of agents are updated according to disease progression rules and whether they are within the hospital area.
   4. Counters for each disease state are updated, and the day's statistics are displayed on the screen.
   5. The matplotlib plot is updated to reflect the new counts.
      
## Installation
To run this simulation, you will need Python installed on your system, along with the following Python packages:
- turtle
- matplotlib
- random
You can install the required packages using pip:

```bash
pip install turtle matplotlib, random, turtle
```
Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/SEIRD-model-simulation.git
cd SEIRD-model-simulation
```

## Usage

Execute the modeler.py script to start the simulation:

```bash
python modeler.py
```
This will open a window displaying the turtle graphics and initiate the simulation. A plot will be generated and saved as SIR.png to visualize the epidemic's progression.

## Customization

The simulation parameters can be adjusted to represent different scenarios. These include the size of the population, the initial number of infected individuals, and the size of specialized areas such as hospitals.

