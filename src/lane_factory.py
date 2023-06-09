from turtle import Turtle
from lanes import Lane


class LaneFactory():
    def __init__(self, num_of_lanes, height_of_screen) -> None:
        self.lanes = []
        self.num_of_lanes = num_of_lanes + 1
        self.height_of_lane = height_of_screen/self.num_of_lanes
        self.initial_y = -height_of_screen/2
        y = self.initial_y
        for i in range(num_of_lanes):
            self.lanes.append(Lane(y, lane_height=self.height_of_lane))
            print(f"y of lane {i} is: {y}")
            y += self.height_of_lane

    def move_cars(self):
        for lane in self.lanes:
            lane.move_cars()
