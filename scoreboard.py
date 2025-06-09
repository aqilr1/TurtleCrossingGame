from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-280,250)
        self.write(f"Score: {self.score}", align='left', font=FONT)


    def end_game(self):
        self.goto(0,0)
        self.write("GAME OVER.", align='center', font=FONT)