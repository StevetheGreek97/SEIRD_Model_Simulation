import random

import turtle

from utils import make_plot, display_counts, update_counter
from box import Box
from agent import Agent


def populate_world(inf_count, sus_count):
    # Create population of agents
    population = []
    
    for _ in range(inf_count):
        population.append(
        Agent(state = 'I', 
              x = random.uniform(-250, 250), 
              y = random.uniform(-250, 250))
        )
        
    for _ in range(sus_count):
        population.append(
            Agent(state = 'S', 
                  x = random.uniform(-250, 250), 
                  y = random.uniform(-250, 250))
            )

    return population


def main(): 
    days = 0 
    susceptible_perday = []
    infected_perday = []
    recovered_perday = []
    exposed_perday = []
    dead_perday = []
    # Define turtle graphics settings
    
    # turn off screen updates for faster rendering
    turtle.tracer(0, 0) 
    # set world coordinates to match screen size
    turtle.setworldcoordinates(-250, -250, 250, 250)  
    turtle.penup()
    turtle.hideturtle()

    # Create box and population
    world = Box(
        width = 1000, 
        height = 600, 
        color = 'lightgrey'
        )

    hospital = Box(
        width = 200,
        height = 200,
        x_offset = -400, 
        y_offset = -200, 
        color = 'lightblue', 
        name  = "  Hospital"
        )
    
    cemetery = Box(
        width = 200,
        height = 200,
        x_offset = 400, 
        y_offset = 200, 
        color = 'grey', 
        name  = "  Cemetery"
        )

    population = populate_world(5, 100)

    # Main simulation loop
    run = True

    while run :
        # count the number of agents in each state
        SEIRD = {
            's': 0,
            'i' : 0,
            'r' : 0,
            'e' : 0,
            'd' : 0
                 }

        days += 1
        # update screen once per loop
        turtle.update() 

        # main for loop iterating through the population       
        for agent in population:
            
            update_counter(agent, SEIRD)
            agent.interact(population)
            agent.update_status()
            agent.update_stats(hospital)
            agent.walk(hospital, cemetery)
            agent.bounce(world)

        susceptible_perday.append(SEIRD['s'])
        infected_perday.append(SEIRD['i'] )
        recovered_perday.append(SEIRD['r'])
        exposed_perday.append(SEIRD['e'])
        dead_perday.append(SEIRD['d'] )
        
        display_counts(
            count = days,
            s = SEIRD['s'], 
            i = SEIRD['i'], 
            r = SEIRD['r'], 
            e = SEIRD['e'],
            d = SEIRD['d']
            )
   
        # stop the simulation
        if SEIRD['i'] == 0 and SEIRD['e'] == 0: #  or days >= 1000
            run = False

    turtle.done()  

    make_plot(
        s = susceptible_perday,
        e = exposed_perday, 
        i = infected_perday, 
        r = recovered_perday,
        d = dead_perday
        )

    
if __name__ == "__main__":
    main()
