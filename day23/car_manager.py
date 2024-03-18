from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 5
STARTING_X = 320

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.move_distance = 5
        self.hideturtle()

    def create_car(self):
        random_chance = random.randint(0,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 251)
            new_car.goto(STARTING_X, random_y)
            self.car_list.append(new_car)


    def car_move(self):
        for car in self.car_list:
            car.backward(self.move_distance)

    def new_level(self):
        for car in self.car_list:
            car.goto(600, 600)
        self.car_list = []
        self.move_distance += MOVE_INCREMENT