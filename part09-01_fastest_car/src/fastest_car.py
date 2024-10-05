class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

def fastest_car(cars: list):
    return max(cars, key=lambda car: car.top_speed).make
