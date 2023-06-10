from turtle import Turtle
from game_configs import *
from car import Car
from car_factory import CarFactory


class Lane(Turtle):
    def __init__(self, y, lane_height) -> None:
        super().__init__(visible=False)
        self.lane_height = lane_height
        self.penup()
        self.pencolor("white")
        self.pensize(2)
        self.setpos(x=LEFT_BORDER, y=y+lane_height)
        while self.xcor() < RIGHT_BORDER:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

        self.cars = []
        self.car_factory = CarFactory()

    def gen_cars(self):
        car = self.car_factory.gen_cars(
            car_x=RIGHT_BORDER + 20, car_y=self.ycor() + self.lane_height/2)
        if car:
            self.cars.append(car)

    def move_cars(self):
        if len(self.cars) > 0:
            for car in self.cars:
                car.move()

    def process_frame(self):
        self.gen_cars()
        self.move_cars()
