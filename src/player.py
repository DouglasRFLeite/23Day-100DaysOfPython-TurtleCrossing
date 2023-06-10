from turtle import Turtle
from game_configs import *


class Player(Turtle):
    def __init__(self, shape: str = "turtle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color("white")
        self.setpos(x=0, y=BOTTOM_BORDER + 35)
        self.seth(90)

    def move(self):
        self.forward(10)
