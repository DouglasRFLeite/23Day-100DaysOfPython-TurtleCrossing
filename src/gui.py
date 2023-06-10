from turtle import Turtle, Screen
from lanes import Lane
from lane_factory import LaneFactory
from car import Car
from game_configs import *
from score import Score


class GUI():
    def __init__(self):
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.setup(600, 400)
        self.screen.bgcolor("black")
        self.screen.listen()

        self.lane_f = LaneFactory(4, SCREEN_HEIGHT)

        self.score = Score()
