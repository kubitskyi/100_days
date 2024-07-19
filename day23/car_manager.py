from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self, possition, color) -> None:
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(possition)
        self.move_speed = STARTING_MOVE_DISTANCE
            

    def move(self, level):
        new_x = self.xcor() - self.move_speed - STARTING_MOVE_DISTANCE * level
        self.goto(new_x, self.ycor())


class CarManager:
    def __init__(self) -> None:
        self.cars = []

    def get_car(self):
        color = random.choice(COLORS)
        ycors = [cor for cor in range(-260,280,20)]
        ycor = random.choice(ycors)
        chance = round(random.uniform(0,1), 2)
        if chance < 0.25:
            self.cars.append(Car((310,ycor),color))

    def cars_move(self, level):
        for car in self.cars:
            car.move(level)

    def get_cars(self):
        return self.cars
    
    def reset_cars(self):
        for car in self.cars:
            car.clear()
        self.cars = []