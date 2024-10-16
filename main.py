from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()
scoreboard = Scoreboard()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")
screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.inc_score()

    if snake.segments[0].xcor() > 270 or snake.segments[0].ycor() > 270 or snake.segments[0].xcor() < -270 or snake.segments[0].ycor() < -270:
        game_is_on = False
        scoreboard.game_over()

# detect collision with tail and call game over

    for new_segment in snake.segments[1::]:
        # if new_segment == snake.segments[0]:
        #     pass

        if snake.segments[0].distance(new_segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()