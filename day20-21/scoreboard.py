from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.score = 0
        self.color("white")
        self.pen(shown=False)
        self.goto(-50, 275)
        self.write(f"Score: {self.score}", font=('Courier', 15))

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align="center", font=('Courier', 30))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", font=('Courier', 15))