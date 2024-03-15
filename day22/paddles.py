from turtle import Turtle

class Paddles(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()

        self.speed("fastest")
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid = 5.0, stretch_len = 1.0)
        self.goto(x_pos, y_pos)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)