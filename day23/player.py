from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color('green')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.left(90)
        self.goto(STARTING_POSITION)
        self.move_speed = MOVE_DISTANCE

    def move_up(self):
        new_y = self.ycor() + self.move_speed
        if new_y < 290:
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - self.move_speed
        if new_y > -290:
            self.goto(self.xcor(), new_y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)