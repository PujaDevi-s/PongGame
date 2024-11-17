from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# creating a screen
screen = Screen()
screen.setup(width= 800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Creating a paddle for both side
paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))

# Creating a ball
ball = Ball()

#Creating a scoreboard
scoreboard = Scoreboard()
screen.listen()

# Giving the up and down keys for moving right paddle 
screen.onkey(fun=paddle_r.up, key="Up")
screen.onkey(fun=paddle_r.down, key="Down")

# Giving the w and s keys for moving left paddle
screen.onkey(fun=paddle_l.up, key="w")
screen.onkey(fun=paddle_l.down, key="s")
game_is_on = True

# Starting the game
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # ball needs to bounce 
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and  ball.xcor() < -320:
        # ball need to bounce    
        ball.bounce_x()
    # Detect when right paddle misses    
    if ball.xcor() > 380:  
        ball.reset_position() 
        scoreboard.l_point()
        
    # Detect when the left paddle misses         
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
screen.exitonclick()
