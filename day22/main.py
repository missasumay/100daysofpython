from turtle import Screen
from paddles import Paddles
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PyPong")
screen.tracer(0)

player = Paddles(350, 0)
opponent = Paddles(-350, 0)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=player.go_up)
screen.onkeypress(key="Down", fun=player.go_down)
screen.onkeypress(key="w", fun=opponent.go_up)
screen.onkeypress(key="s", fun=opponent.go_down)


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(player) < 50 and ball.xcor() > 320 or ball.distance(opponent) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_for_opponent()
        score.add_score("opponent")
    elif ball.xcor() < -380:
        ball.reset_for_player()
        score.add_score("player")









screen.exitonclick()