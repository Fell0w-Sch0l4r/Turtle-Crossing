from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) -> None:
        self.cars: list[Turtle] = []
        self.cars1: list[Turtle] = []
        
        self.creat_car()
        
        
    def creat_car(self):
        for _ in range(50):
            car: Turtle = Turtle(shape="square")
            car.penup()
            car.shapesize(stretch_len=2)
            car.color(choice(COLORS))
            car.setpos(320, randint(-260, 250))
            
            self.cars.append(car)
            
    def show_car(self):
        lista = [True, False]
        can_show_car: bool = choice(lista)
        
        if can_show_car:
            if len(self.cars) >= 1:
                self.cars1.append(self.cars[0])
                self.cars.pop(0)
        

    def move_cars(self):
        if len(self.cars1) >= 1:
            for car in self.cars1:
                car.backward(5)