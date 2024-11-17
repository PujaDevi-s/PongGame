from turtle import Turtle
class Paddle(Turtle):

    # creating a paddle 

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("grey")
        self.penup()
        self.goto(position)

    # Moving the paddle upside
        
    def up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(),y)

    # Moving the paddle downside

    def down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(),y)        
