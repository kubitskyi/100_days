from turtle import Turtle


ALIGN = "center"
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.right_count = 0 
        self.left_count = 0 
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.update_scoreboard()
        self.hideturtle()

    def game_over(self):
         self.goto(0,0)
         self.write(f"Game Over!", align=ALIGN, font=FONT)

    def update_scoreboard(self):
        self.write(f"{self.left_count} : {self.right_count}", align=ALIGN, font=FONT)

    def right_point(self):
        self.right_count += 1 
        self.clear()
        self.update_scoreboard()

    def left_point(self):
        self.left_count += 1 
        self.clear()
        self.update_scoreboard()