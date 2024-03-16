from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
starting_positions = [(0,0), (-20, 0), (-40,0)]


class Snake():

    def __init__(self):
        self.wensze = []

        self.create_wonsz()

        self.head = self.wensze[0]

    def create_wonsz(self):
        for position in starting_positions:
            self.add_wonsz(position)

    def extend(self):
        self.add_wonsz(self.wensze[-1].position())

    def add_wonsz(self, position):
        self.nowy_wonsz = Turtle("square")
        self.nowy_wonsz.color("lime green")
        self.nowy_wonsz.penup()
        self.nowy_wonsz.goto(position)
        self.wensze.append(self.nowy_wonsz)

    def move(self):

        for wonsz in range(len(self.wensze) - 1, 0, -1):
            self.new_x = self.wensze[wonsz - 1].xcor()
            self.new_y = self.wensze[wonsz - 1].ycor()
            self.wensze[wonsz].goto(self.new_x, self.new_y)
        self.head.forward(10)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for wonsz in self.wensze:
            wonsz.goto(1000, 1000)
        self.wensze.clear()
        self.create_wonsz()
        self.head = self.wensze[0]