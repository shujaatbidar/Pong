from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.count = 0
        self.r_count = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.write(f"{self.count}         {self.r_count}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"{self.count}         {self.r_count}", align=ALIGNMENT, font=FONT)

    def update_score_right(self):
        self.count += 1
        self.clear()
        self.update_score()

    def update_score_left(self):
        self.r_count += 1
        self.clear()
        self.update_score()



