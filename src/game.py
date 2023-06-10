from turtle import Turtle, Screen
from gui import GUI
from lanes import Lane
from lane_factory import LaneFactory
from game_configs import *
from time import sleep
from player import Player


def main():
    gui = GUI()

    gui.screen.update()
    player = Player()
    gui.screen.update()

    gui.screen.onkeypress(key="Up", fun=player.move)

    while True:
        sleep(0.1)
        gui.lane_f.process_frame()
        gui.screen.update()

    gui.screen.exitonclick()


if __name__ == "__main__":
    main()
