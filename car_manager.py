from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) -> None:
        self.invisible_cars: list[Turtle] = []
        self.visible_cars: list[Turtle] = []
        
        self.creat_cars(num_of_cars=45)
        
        self.playtime = 0.1
        
        
    def creat_cars(self, num_of_cars: int):
        for _ in range(num_of_cars):
            car: Turtle = Turtle(shape="square")
            car.penup()
            car.shapesize(stretch_len=2)
            
            self.modify_car(car)
            
            self.invisible_cars.append(car)
            
            
    def can_show_car(self) -> bool:
        return choice([True, False]) 
    
          
    def show_car(self):
        if self.can_show_car():
            if len(self.invisible_cars) >= 1:
                self.visible_cars.append(self.invisible_cars[0])
                self.invisible_cars.pop(0)
        

    def move_cars(self):
        self.show_car()
        self.shift_cars()
        
        for car in self.visible_cars:
            car.backward(5)
                
    
    def get_hiden_cars_indexes(self) -> list:
        hiden_cars_index=[]
        for index in range(len(self.visible_cars)):
            if self.visible_cars[index].xcor() <= -320:
                hiden_cars_index.append(index)
                
        return hiden_cars_index  
    
     
    
    def set_random_position(self, car: Turtle):
        car.setpos(x=320, y=randint(-250, 250))
          
        
    def set_random_color(self, car: Turtle):
        car.color(choice(COLORS))
        
        
    def modify_car(self, car: Turtle):
        """Changes the color and the position
        of the car.

        Args:
            car (Turtle): The car
        """
        self.set_random_color(car)
        self.set_random_position(car)
        
                
    def shift_cars(self):
        hiden_cars_indexes = self.get_hiden_cars_indexes()   
                
        if len(hiden_cars_indexes) >= 1:
            for index in hiden_cars_indexes:
                car: Turtle = self.visible_cars[index]
                self.modify_car(car)
                
                
                self.invisible_cars.append(car)
                self.visible_cars.pop(index)
                
                
                
    def colided_with_player(self, player: Turtle) -> bool:
        for car in self.visible_cars:
            if car.xcor() <= 20:
                if car.distance(player) < 20:
                    return True
                
                
    def increase_cars_speed(self):
        self.playtime *= 0.9