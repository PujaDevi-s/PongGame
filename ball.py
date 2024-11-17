from turtle import Turtle
class Ball(Turtle):

    # create a ball and set the speed and movement
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.3

    # moving the ball    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # creating bounce effect in yaxis
    def bounce_y(self):
        self.y_move *= -1
    
    # creating bounce effect in xaxis
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # reset the ball to the center original position and speed
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.3
        self.bounce_x()
