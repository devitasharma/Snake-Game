import time
from turtle import Screen
from Food import Food
from Snake_making_and_movement import SnakeMakingAndMoving
from ScoreBoard import Score
from tkinter import messagebox

screen = Screen()

"""Setting up panel by providing panel frame size + panel title + panel background colour."""
screen.setup(600, 600)
screen.bgcolor("#01204E")
screen.title("My first Snake Game.")
screen.tracer(0)
screen.update()

Nagg = SnakeMakingAndMoving()
food = Food()
score = Score()
new_high_score = 0

"""moving snake in continuous forward position."""
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    Nagg.snake_movement()
    if Nagg.snake_head.distance(food) < 15:
        food.refresh()
        Nagg.extend_snake()
        score.score_track()

    elif (Nagg.snake_head.xcor() > 280 or Nagg.snake_head.xcor() < -280 or Nagg.snake_head.ycor() > 280
          or Nagg.snake_head.ycor() < -280):
        messagebox.showinfo(title="OOp's", message="GAME OVER!")
        score.reset_score()
        Nagg.reset()

        """ Below is the use of slicing method:"""
    for saap in Nagg.snakes[1:]:
        if Nagg.snake_head.distance(saap) < 10:
            messagebox.showinfo(title="OOp's", message="GAME OVER!")
            score.reset_score()
            Nagg.reset()
            # is_game_on = False
            # score.game_over()

    # for saap in Nagg.snakes:

    # if saap == Nagg.snake_head:
    #     pass
    # elif Nagg.snake_head.distance(saap) < 10:
    #     is_game_on = False
    #     score.game_over()

    screen.listen()
    screen.onkey(fun=Nagg.up, key="Up")
    screen.onkey(fun=Nagg.down, key="Down")
    screen.onkey(fun=Nagg.right, key="Right")
    screen.onkey(fun=Nagg.left, key="Left")

screen.exitonclick()
