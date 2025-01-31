from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

def get_data():
    with open('data.txt') as f:
        return int(f.read())
       

def set_data(data):
    with open('data.txt', 'w') as f:
        f.write(data)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = get_data()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self) -> None:
        if self.high_score < self.score:
            self.high_score = self.score
            set_data(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
