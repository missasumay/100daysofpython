from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)
screen = Screen()
screen.setup(width=700, height=300)

x = -320
y = -100
name_id = 0
is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a name:\n(janusz, marian, bogdan, stefan, staszek, bartek)")

janusz = Turtle()
marian = Turtle()
bogdan = Turtle()
stefan = Turtle()
staszek = Turtle()
bartek = Turtle()

zolwiki = [janusz, marian, bogdan, stefan, staszek, bartek]
zolwiki_imiona = ["janusz", "marian", "bogdan", "stefan", "staszek", "bartek"]

for zolw in zolwiki:
    zolw.shape("turtle")
    zolw.color((random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255)))
    zolw.penup()
    zolw.goto(x, y)
    zolw.pendown()
    zolw.write(zolwiki_imiona[name_id])
    y += 40
    name_id += 1

if user_bet:
    is_race_on = True

for imiona in range(0,6):
    if user_bet == zolwiki_imiona[imiona]:
        user_turtle = zolwiki[imiona]



while is_race_on:
    for zolw in zolwiki:
        if zolw.xcor() > 340:
            is_race_on = False
            if zolw == user_turtle:
                print(f"Your turtle {user_bet} has won, congratulations!")
            else:
                print(f"{user_bet} has lost!")
        else:
            rand_distance = random.randint(0,15)
            zolw.forward(rand_distance)

screen.exitonclick()