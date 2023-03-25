from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) -> None:
        self.invisible_cars: list[Turtle] = []
        self.visible_cars: list[Turtle] = []
        
        self.creat_cars()
        
        
    def creat_cars(self):
        for _ in range(30):
            car: Turtle = Turtle(shape="square")
            car.penup()
            car.shapesize(stretch_len=2)
            car.color(choice(COLORS))
            car.setpos(320, randint(-250, 250))
            
            self.invisible_cars.append(car)
            
    def show_car(self):
        lista = [True, False, False, False]
        can_show_car: bool = choice(lista)
        
        if can_show_car:
            if len(self.invisible_cars) >= 1:
                self.visible_cars.append(self.invisible_cars[0])
                self.invisible_cars.pop(0)
        

    def move_cars(self):
        if len(self.visible_cars) >= 1:
            for car in self.visible_cars:
                car.backward(5)
                
    def shift_cars(self):
        
        hiden_cars=[]
        for index in range(len(self.visible_cars)):
            if self.visible_cars[index].xcor() <= -320:
                hiden_cars.append(index)
                
        if len(hiden_cars) >= 1:
            for index in hiden_cars:
                self.visible_cars[index].color(choice(COLORS))
                self.visible_cars[index].setpos(320, randint(-250, 250))
                
                self.invisible_cars.append(self.visible_cars[index])
                self.visible_cars.pop(index)
                #you're changing the size of the list while you're still
                #iterating it
                
                
    def colided(self, player: Turtle) -> bool:
        for car in self.visible_cars:
            if car.xcor() <= 20:
                if car.distance(player) < 20:
                    return True