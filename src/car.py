from turtle import Turtle
from game_configs import *
import random

car_colors = ["red", "blue", "green", "yellow",
              "orange", "purple", "pink", "brown", "gray", "white"]


class Car(Turtle):
    def __init__(self, x, y, move_speed=5) -> None:
        super().__init__(shape="square")
        self.color(random.choice(car_colors))
        self.penup()
        self.move_speed = move_speed
        self.seth(180)
        self.setpos(x=x, y=y)
        self.shapesize(stretch_len=2, stretch_wid=1)

    def move(self):
        self.forward(self.move_speed)
