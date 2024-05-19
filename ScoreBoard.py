from turtle import Turtle
ALLIGNMENT = "center"
FONT =("Courier",15,"bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open("High_Score.py", mode="r") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_score_board()
        self.hideturtle()
        print(f"in init{self.high_score}")

    def update_score_board(self):
        self.clear()
        self.write(f"Score={self.score} High Score={self.high_score}", align=ALLIGNMENT, font=FONT)
    def score_track(self):
        self.score += 1
        self.update_score_board()
    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("High_Score.py", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score_board()












