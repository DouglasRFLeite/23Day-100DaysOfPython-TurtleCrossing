from turtle import Turtle
from game_configs import *
from car import Car


class Lane(Turtle):
    def __init__(self, y) -> None:
        super().__init__(visible=False)
        self.penup()
        self.pencolor("white")
        self.pensize(2)
        self.setpos(x=LEFT_BORDER, y=y)
        while self.xcor() < RIGHT_BORDER:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

        self.car1 = Car(x=RIGHT_BORDER, y=self.ycor() + 5)
