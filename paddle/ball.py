from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        self.directiony = 8
        self.directionx = 8
        self.speedx = 1
        self.speedy = 1
        super().__init__()
        self.create_ball()
        self.move_speed = 0.1

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1, outline=1)
        self.penup()
        self.goto(0, 0)

    def move(self):
        newx = self.xcor() + (self.directionx * self.speedx)
        newy = self.ycor() + (self.directiony * self.speedy)
        self.goto(newx, newy)

    def bounce(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.directiony = self.directiony * -1
            self.speedy *= 1.1

        if 320 < self.xcor() < 370 or -320 > self.xcor() > -370:
            self.directionx = self.directionx * -1
            self.speedx *= 1.1
            self.move_speed *= 0.9

        if self.xcor() > 390 or self.xcor() < -390:
            self.directionx = self.directionx * -1

    def reset_ball(self):
        self.bounce()
        self.move_speed = 0.1
        self.goto(0, 0)





