from turtle import Turtle
from game_configs import *


class Car(Turtle):
    def __init__(self, x, y) -> None:
        super().__init__(shape="square")
        self.color("white")
        self.penup()
        self.move_speed = 5
        self.seth(180)
        self.setpos(x=x, y=y)

    def move(self):
        self.forward(self.move_speed)
