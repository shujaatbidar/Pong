from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(800, 600)
screen.listen()
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(False)
paddle = Paddle((350, 0))
score = Scoreboard()

second_paddle = Paddle((-350, 0))

ball = Ball()


screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")

screen.onkey(second_paddle.up, "w")
screen.onkey(second_paddle.down, "s")

game = True


def is_hitting_ceiling_or_floor(theball):
    return theball.ycor() > 290 or theball.ycor() < -290


LEFT_WALL_XCORD = 320


while game:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if is_hitting_ceiling_or_floor(ball):
        ball.bounce()

    if ball.distance(paddle) < 50 and ball.xcor() > LEFT_WALL_XCORD or ball.distance(second_paddle) < 50 and ball.xcor() < -LEFT_WALL_XCORD:
        ball.bounce()

    if ball.xcor() > 390:
        score.update_score_right()
        ball.reset_ball()

    if ball.xcor() < -390:
        score.update_score_left()
        ball.reset_ball()


screen.exitonclick()

