from turtle import Turtle, Screen
from gui import GUI
from lanes import Lane
from lane_factory import LaneFactory
from game_configs import *
from time import sleep


def main():
    gui = GUI()

    gui.screen.update()

    while True:
        sleep(0.1)
        gui.lane_f.move_cars()
        gui.screen.update()

    gui.screen.exitonclick()


if __name__ == "__main__":
    main()
