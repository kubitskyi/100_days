from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

PL1POS, PL2POS = (-380, 0), (370, 0)
TIME_SLEEP = 0.1

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong")
screen.tracer(0)

left_player = Paddle(PL1POS)
right_player = Paddle(PL2POS)

scrore = Scoreboard()
ball = Ball()

screen.listen()
screen.onkey(left_player.go_up, "w")
screen.onkey(left_player.go_down,"s")
screen.onkey(left_player.go_up, "W")
screen.onkey(left_player.go_down,"S")
screen.onkey(right_player.go_up, "Up")
screen.onkey(right_player.go_down,"Down")


game_is_on = True
while game_is_on:
    

    screen.update()
    time.sleep(TIME_SLEEP)
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < - 280:
        # needs to bounce
        ball.bounce_y()

    #Detect collision with right player
    if ball.distance(right_player) < 50 and ball.xcor() > 340:
        ball.bounce_x()
    elif ball.distance(left_player) < 50 and ball.xcor() < - 340:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scrore.left_point()
    
    if ball.xcor() < -380:
        ball.reset_position()
        scrore.right_point()
    

screen.exitonclick()