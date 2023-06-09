from turtle import Turtle
from lanes import Lane


class LaneFactory():
    def __init__(self, num_of_lanes, height_of_screen) -> None:
        self.lanes = []
        self.num_of_lanes = num_of_lanes + 1
        self.height_of_lane = height_of_screen/num_of_lanes
        self.initial_y = -height_of_screen/2
        y = self.initial_y
        for _ in range(num_of_lanes):
            self.lanes.append(Lane(y))
            y += self.height_of_lane
