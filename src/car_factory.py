from car import Car
import random


class CarFactory():
    def __init__(self):
        pass

    def gen_cars(self, car_x, car_y, move_speed=5, cars_per_lane=4):
        if random.randint(0, 100) < cars_per_lane:
            return Car(car_x, car_y, move_speed)
