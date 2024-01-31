from turtle import Turtle


class Ball(Turtle):

    def __init__( self ):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10  # when the ball hit the down wall it should bounce up, this can do by adding 10 to the y cor
        self.y_move = 10  # when the ball hit the top we should bounce it down for that we use bounce method
        self.ball_speed = 0.1

    def move( self ):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x , new_y)

    def bounce_y( self ):
        self.y_move *= -1


    def bounce_x( self ):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position( self ):
        self.goto(0,0)
        self.x_move *= -1
        self.ball_speed = 0.1