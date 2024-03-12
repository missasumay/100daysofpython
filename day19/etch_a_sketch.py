from turtle import Turtle, Screen

zolwik = Turtle()
screen = Screen()
zolwik.shape("turtle")
zolwik.color("green")

def go_forward():
    zolwik.forward(10)

def go_backwards():
    zolwik.back(10)

def go_right():
    zolwik.right(15)

def go_left():
    zolwik.left(15)

def clear_screen():
    zolwik.clear()
    zolwik.penup()
    zolwik.home()
    zolwik.pendown()


screen.listen()
screen.onkey(key="w", fun=go_forward)
screen.onkey(key="s", fun=go_backwards)
screen.onkey(key="a", fun=go_left)
screen.onkey(key="d", fun=go_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()