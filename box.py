import turtle

class Box(turtle.Turtle):
    """
    Class for drawing the simulation box.
    """
    
    def __init__(
        self, 
        width, 
        height, 
        name = '', 
        x_offset = 0 , 
        y_offset = 0, 
        color = 'white'
                 ):
        """
        Initialize the box with given width and height.
        """
        super().__init__()
        self.x = -width/2 + x_offset
        self.y = -height/2 + y_offset
        self.width = width
        self.height = height
        self.penup()
        self.setpos(self.x, self.y)
        self.begin_fill()
        self.fillcolor(color)
        self.write(name,align='left', font=("Arial", 16, "normal"))
        self.pendown()
        for _ in range(2):
            self.forward(width)
            self.left(90)
            self.forward(height)
            self.left(90)
        self.end_fill()

            
