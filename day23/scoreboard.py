from turtle import Turtle
import time


FONT = ("Courier", 24, "normal")
ALIGN = "left"

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level = 1 
        self.color("black")
        self.penup()
        self.goto(-260,260)
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def level_up(self):
        self.level += 1
    
    def get_level(self):
        return self.level

    def reset_level(self):
        self.level = 1

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=FONT)
        self.reset_level()

