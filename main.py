from snake import *
from food import Food
import turtle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("My snake game")
turtle.goto(-50,280)
turtle.color("white")
turtle.hideturtle()

screen.tracer(0)
snake1 = Snake()
food1 = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake1.up,"Up")
screen.onkey(snake1.down,"Down")
screen.onkey(snake1.left,"Left")
screen.onkey(snake1.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake1.move()
    
    if(snake1.head.distance(food1) < 15):
        food1.food_refresh()
        score.increase_score()
        food1 = Food()
        snake1.extend()

    if snake1.head.ycor() > 280 or snake1.head.ycor() < -280 or  snake1.head.xcor() > 280 or snake1.head.xcor() < -280:
        game_is_on = False
        score.lost()

screen.exitonclick()