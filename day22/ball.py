from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.speed('normal')
        self.goto(0,0)
        self.move_x = random.choice([10,-10])
        self.move_y = random.choice([10,-10])
        

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.move_y *= -1
    
    def bounce_x(self):
        self.move_x *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()