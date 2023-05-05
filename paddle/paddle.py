from turtle import Turtle
MOVE_FORWARD = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.left(90)
        self.shapesize(stretch_wid=1, stretch_len=5, outline=1)
        self.penup()
        self.goto(position)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)





