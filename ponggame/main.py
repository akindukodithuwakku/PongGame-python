from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

'''creating the screen'''
WIDTH = 800
HEIGHT = 600
screen = Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH , height=HEIGHT)
screen.title('Pong Game')
screen.tracer(0)

'''creating the paddles'''

l_paddle = Paddle((-390 , 0))
r_paddle = Paddle((380 , 0))

'''creating the ball'''
ball = Ball()
screen.listen()
screen.onkey(r_paddle.go_up , "Up")
screen.onkey(r_paddle.go_down , "Down")

screen.onkey(l_paddle.go_up , "w")
screen.onkey(l_paddle.go_down , "s")

'''creating the score board object'''
score = Score()


game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # detect collision with wall up and down
    if ball.ycor() > 295 or ball.ycor() < -295:
        ball.bounce_y()

    # detect collision with a paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 360 or ball.distance(l_paddle) < 50 and ball.xcor() < -370:
        ball.bounce_x()

    # detect missing of paddles
    if ball.xcor() > 390:
        ball.reset_position()
        score.score_left()

    if ball.xcor() < -390:
        ball.reset_position()
        score.score_right()


screen.exitonclick()
