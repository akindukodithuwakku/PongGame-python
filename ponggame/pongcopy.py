from turtle import Screen, Turtle

WIDTH = 800
HEIGHT = 600
screen = Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.title('Pong Game')

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_len=1, stretch_wid=5)
paddle.penup()
paddle.goto(x=-390, y=0)

def move_paddle(y):
    paddle.goto(-390, y)

def handle_click(x, y):
    move_paddle(y)

screen.onclick(handle_click)

screen.mainloop()
