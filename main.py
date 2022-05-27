from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)
game_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

while game_on:
    screen.update()
    time.sleep(.05)
    snake.move()
    if snake.head.distance(food) < 15:
        food.random_pos()
        scoreboard.get_score()
        snake.extend_segment()
    
    #detect collision with wall
    if (snake.head.xcor() > 300 or snake.head.xcor() < -300 or
        snake.head.ycor() > 300 or snake.head.ycor() < -300):
        scoreboard.game_over()
        game_on = False
    
    #detect collision with segment
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_on = False
            
screen.exitonclick()
