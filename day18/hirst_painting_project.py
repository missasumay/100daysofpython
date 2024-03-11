from turtle import Turtle, Screen
import turtle as t
import random

timmy_the_turtle = Turtle()
screen = Screen()
t.colormode(255)

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("lime green")


directions = [0, 90, 180, 270]

timmy_the_turtle.speed("fastest")

x = -450
y = -450

timmy_the_turtle.penup()
timmy_the_turtle.setposition(-450, -400)
timmy_the_turtle.pendown()

for _ in range (30):
    timmy_the_turtle.penup()
    timmy_the_turtle.setposition(x, y)
    timmy_the_turtle.pendown()
    y += 30

    for _ in range (30):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        timmy_the_turtle.color(r, g, b)
        timmy_the_turtle.pensize(15)
        timmy_the_turtle.dot(15)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(30)
        timmy_the_turtle.pendown()

screen.exitonclick()