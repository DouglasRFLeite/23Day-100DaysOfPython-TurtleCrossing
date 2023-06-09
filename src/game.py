from turtle import Turtle, Screen
from gui import GUI
from lanes import Lane
from lane_factory import LaneFactory
from game_configs import *


def main():
    gui = GUI()

    gui.screen.tracer(1)

    while True:
        gui.lane_f.lanes[0].car1.move()

    gui.screen.exitonclick()


if __name__ == "__main__":
    main()
