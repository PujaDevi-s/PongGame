from turtle import Turtle

class Scoreboard(Turtle):

    #creating scoreboard

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    # Updating the score board after the score increases

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
           
    # Adding score to left side

    def l_point(self):
        self.l_score+=1    
        self.update_scoreboard()

    # Adding score to right side
        
    def r_point(self):
        self.r_score+=1    
        self.update_scoreboard()
