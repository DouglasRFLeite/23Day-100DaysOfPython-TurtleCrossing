from turtle import Turtle
from game_configs import *


class Score(Turtle):

    def __init__(self) -> None:
        super().__init__("square", 1000, False)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(x=LEFT_BORDER + 30, y=BOTTOM_BORDER + 35)

        self.level = 1

        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left",
                   font=('Courier', 14, 'normal'))

    def update_score(self):
        self.level += 1
        self.write_score()

    def game_over(self):
        self.clear()
        self.setpos(0, 0)
        self.write(f"Game Over!", align="center",
                   font=('Courier', 30, 'normal'))
        self.setpos(0, -40)
        self.write(f"Your final score was: {self.level}", align="center",
                   font=('Courier', 18, 'normal'))
