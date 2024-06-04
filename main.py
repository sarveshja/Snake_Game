from turtle import Screen
import time
from snake import Snake
from food import  Food
from scoreboard import ScreBoard

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")

screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
game_is_on = True

while(game_is_on):
    screen.update()
    time.sleep(0.2)
    snake.move()

    if(snake.head.distance(food) < 15):
        food.refresh()
        snake.extend()
        score.increasescore()

    if(snake.head.xcor() > 250 or snake.head.xcor() < -250 or snake.head.ycor() > 250 or snake.head.ycor() < -250):
        game_is_on = False
        score.game_over()

    for i in range(1, len(snake.snake)-1):
        if(snake.head.distance(snake.snake[i])<10):
            game_is_on = False
            score.game_over()
screen.exitonclick()

