from turtle import Turtle


class Score(Turtle):
    def __init__( self ):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_r = 0
        self.score_l = 0
        self.update()


    def update( self ):
        self.clear()
        self.goto(-100 , 200)
        self.write(f"{self.score_l}" , align="center" , font=("Arial" , 40 , "normal"))
        self.goto(100 , 200)
        self.write(f"{self.score_r}" , align="center" , font=("Arial" , 40 , "normal"))

    def score_left( self ):
        self.score_l += 1
        self.update()

    def score_right( self ):
        self.score_r += 1
        self.update()
