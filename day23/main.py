import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.get_car()
    carmanager.cars_move(scoreboard.get_level())
    scoreboard.update_scoreboard()

    # Fnish check
    if player.ycor() >= FINISH_LINE_Y:
        scoreboard.level_up()
        player.go_to_start()
        screen.update()


    #Detect collision with cars
    for car in carmanager.get_cars():
        if car.distance(player) < 20:
            scoreboard.game_over()
            screen.update()
            time.sleep(2)
            screen.clear()
            carmanager.reset_cars()
            player.go_to_start()
            game_is_on = False