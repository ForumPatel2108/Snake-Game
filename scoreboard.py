from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Your Score : {self.count}",align="center",font=("Arial", 24, "normal"))

    def increase_score(self):
        self.clear()
        self.count += 1
        self.update_scoreboard()

    def lost(self):
        self.goto(0,0)
        self.write(f"You Lost",align="center",font=("Arial", 24, "normal"))


