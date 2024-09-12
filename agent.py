import turtle
import random
import math
from box import Box

class Agent(turtle.Turtle):
    """
    A class for simulating an agent in the population.

    Attributes:
        state (str): The current state of the agent (S = susceptible, I = infected, R = recovered, E = exposed, D = dead).
        size (int): The size of the agent.
        treatment_points (int): The number of points received for being treated at the hospital.
        is_exposed (int): The number of days the agent has been exposed.
        is_infected (int): The number of days the agent has been infected.
        is_recovered (int): The number of days the agent has been recovered.
        speed (int): The speed at which the agent moves.
    """
    id = 0

    def __init__(self, state: str, x: int =0, y: int=0):
        """
        Initialize an agent with given state and position.

        Args:
            state (str): The initial state of the agent 
            (S = susceptible, I = infected, R = recovered, E = exposed, D = dead).
            x (int, optional): The initial x position of the agent. Defaults to 0.
            y (int, optional): The initial y position of the agent. Defaults to 0.
        """
        super().__init__()
        Agent.id += 1
        self.state = state
        self.id = Agent.id
        self.size = 5
        self.treatment_points = 0
        self.is_exposed = 0 
        self.is_infected = 0 
        self.is_recovered = 0 
        self.speed = 2
        self.shape("turtle")

        # Set the color of the agent based on its state
        match state:
            case "S":
                self.color("blue")
            case "I":
                self.color("red")
            case 'E':
                self.color('orange')
            case "R":
                self.color("green")
            case 'D':
                self.color('black')
        
        self.exp2inf = random.normalvariate(70, 20) 
        self.inf2rec = random.normalvariate(500, 200)
        self.rec2sus = random.normalvariate(150, 20)   
        self.inf2dead = random.normalvariate(120, 20) 
        self.penup()
        self.setpos(x, y)
        # self.speed('fastest')  # set turtle speed to fastest

    def is_in(self, room: Box) -> bool:
        """
        Check if the agent has reached a room.

        Args:
            room (turtle.Turtle): The turtle representing a room.

        Returns:
            bool: True if the agent has reached the room, False otherwise.
        """
        x, y = self.position()
        x_room, y_room= room.position()
        
        if (x_room + room.width > x > x_room ) and \
           (y_room + room.height > y > y_room):
            return True
        else:
            return False

    def update_stats(self, hospital: Box) -> None:
        """
        Update the agent's statistics based on its current state.

        Args:
            hospital (turtle.Turtle): The turtle representing the hospital.
        """
        # Update the statistics based on the current state of the agent
        if self.state == 'I':
            self.is_infected += 1
            self.is_exposed = 0
            if self.is_in(hospital):
                self.treatment_points += 100
            else: 
                self.treatment_points += 0
                
        elif self.state == 'E':
            self.is_exposed += 1

        elif self.state == 'R':
            self.is_infected = 0 
            self.is_recovered += 1

        elif self.state == 'S':
            self.treatment_points = 0
            self.is_recovered = 0 

    def update_status(self):
        """
        Update the agent's state 

        """
        # From 'E' to 'I'
        if self.is_exposed >= self.exp2inf: 
            self.state = 'I'
            self.color('red')
           
        # From 'I' to 'R'
        if self.treatment_points >= self.inf2rec:
            self.state = 'R'
            self.color('green')
            
        # From 'R' to 'S'
        if self.is_recovered >= self.rec2sus:
            self.state = 'S'
            self.color('blue')

        # From 'I' to 'D'
        if self.is_infected >= self.inf2dead:
            self.state = 'D'
            self.color('black')

    def head_to(self, destination: Box):
        #calculate the angle between the current position of the agent 
        # and the position of the destination 
        dx = destination.xcor()   - self.xcor()
        dy = destination.ycor()  - self.ycor()
        angle = math.atan2(dy, dx)
        # Add some randomness to the angle to make the movement more natural
        angle += random.uniform(-1, 1)
        # Convert the angle from radians to degrees 
        return angle * 180 / math.pi

    def walk(self, hospital: Box, cemetery: Box):
        """
        Move the agent towards the hospital if infected, otherwise move randomly.

        Args:
            hospital (turtle.Turtle): The turtle representing the hospital.
        """
        match self.state: 
            case "I":

                if not self.is_in(hospital):

                    self.setheading(self.head_to(hospital))
                    # Move the agent forward at its speed
                    self.forward(self.speed) 
                else:
                    pass
                
            case 'D':
                if self.is_in(cemetery):
                    pass
                else:
                    x, y = cemetery.position()
                    self.goto(
                random.uniform(x , x + cemetery.width),
                random.uniform(y , y +  cemetery.height),
                )  
            case _:
                # add some randomness to the heading to make the movement more random
                self.setheading(self.heading() + random.uniform(-45, 45))
                self.forward(random.uniform(0, 10))
            
    def distance(self, other):
        """
        Calculate the distance between this agent and another agent.
        """
        x1, y1 = self.position()
        x2, y2 = other.position()
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def infect(self, other: 'Agent', infectivity: float):
        """
        Check if this agent collides with another agent, and infect or recover as appropriate.

        Parameters:
        other (Agent): the other agent to check collision with
        infectivity (float): the radius within whvision_pointsich this agent can infect others

        Returns:
        bool: True if a collision occurred and the state of one or both agents changed, False otherwise
        """
        if self.distance(other) < self.size + other.size + infectivity:
            if self.state == "I" and other.state == "S":
                other.state = "E"
                other.color("orange")
            elif self.state == "S" and (other.state == "I" or other.state == 'E'):
                self.state = "E"
                self.color("orange")
            return True
        else:
            return False
    
    def collides_with(self, other: 'Agent', vision_points = 10) :
        
        if other.state == 'I':
            vision_points = vision_points
        elif other.state == 'I' and self.state == 'I': 
            vision_points = 0
        elif other.state == 'D' and self.state == 'D':
            vision_points = -50
        
        else:
            vision_points = 0
            
        return vision_points
              
   
    def avoid(self, other: 'Agent', vision_points: int = 10 ):
        """
        Move away from another agent if it is infected.

        Parameters:
        other (Agent): the other agent to avoid collision with

        Returns:
        bool: True if the agent moved away from the other agent, False otherwise
        # """
              
        dist = self.distance(other)
        if dist  < self.size + other.size + self.collides_with(other, vision_points=vision_points):
            self.left(180)
            other.left(90)
            self.forward(5)
            # other.forward(5)
    
            return True
        else:
            return False

    def bounce(self, box: Box):
        """
        Bounces the agent off the edges of the simulation box.

        Args:
        - box: A Box object representing the simulation box.

        Returns:
        - None.
        """
        x, y = self.position()
        if self.state != 'D':
            if abs(x) >= box.width/2 - self.size:
                self.left(180)
                self.setx(math.copysign(box.width/2 - self.size, x))
            if abs(y) >= box.height/2 - self.size:
                self.left(180)
                self.sety(math.copysign(box.height/2 - self.size, y))
            

    def interact(self, population: list):
        for other in population:
            if self != other:
                self.avoid(other, 10)
                self.infect(other, 10)



    def __str__(self):
        return self.id
