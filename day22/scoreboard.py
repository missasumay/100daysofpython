from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.opponent_score = 0
        self.player_score = 0
        self.goto(0, 180)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write((f"{self.opponent_score}:{self.player_score}"), align="center", font=("Courier", 70, "bold"))

    def add_score(self, who):
        if who == "player":
            self.player_score += 1
            self.update_score()
        elif who == "opponent":
            self.opponent_score += 1
            self.update_score()
