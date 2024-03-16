from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.score = 0
        with open('day24/snake/data.txt', mode="r+") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.pen(shown=False)
        self.goto(0, 275)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Courier', 15, "bold"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Courier', 15, "bold"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('day24/snake/data.txt', mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Courier', 15, "bold"))