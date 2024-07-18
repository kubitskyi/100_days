from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, possition):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(possition)
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.speed('fastest')


    def go_up(self):
        new_y = self.ycor() + 20 
        if new_y < 260:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20 
        if new_y > -260:
            self.goto(self.xcor(), new_y)