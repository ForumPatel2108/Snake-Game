from turtle import Turtle, Screen
import random

screen = Screen()

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        x_cord = random.randint(-280,280)
        y_cord = random.randint(-280,280)
        self.goto(x_cord,y_cord)

    def food_refresh(self):
        self.hideturtle()