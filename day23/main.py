import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
car_manager = CarManager()

screen.listen()

screen.onkeypress(key="Up", fun=player.move)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.car_move()

    for car in car_manager.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
            screen.exitonclick()

    if player.ycor() >= 300:
        score.level_completed()
        player.reset_level()
        car_manager.new_level()

