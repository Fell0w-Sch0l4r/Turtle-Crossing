from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) -> None:
        self.invisible_cars: list[Turtle] = []
        self.visible_cars: list[Turtle] = []
        
        self.create_cars(num_of_cars=45)
        
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_cars(self, num_of_cars: int):
        for _ in range(num_of_cars):
            car: Turtle = Turtle(shape="square")
            car.penup()
            car.shapesize(stretch_len=2)
            
            self.set_car(car)
            
            self.invisible_cars.append(car)

    @staticmethod
    def can_show_car() -> bool:
        if randint(1, 6) == 1:
            return True
          
    def show_car(self):
        if self.can_show_car():
            if len(self.invisible_cars) >= 1:
                self.visible_cars.append(self.invisible_cars[0])
                self.invisible_cars.pop(0)

    def move_cars(self):
        self.show_car()
        self.shift_cars()
        
        for car in self.visible_cars:
            car.backward(self.move_speed)

    def get_hidden_cars_indexes(self) -> list:
        hidden_cars_index = []
        for index in range(len(self.visible_cars)):
            if self.visible_cars[index].xcor() <= -320:
                hidden_cars_index.append(index)
                
        return hidden_cars_index
    
    @staticmethod
    def set_car_position(car: Turtle):
        car.setpos(x=320, y=randint(-240, 240))

    @staticmethod
    def set_car_color(car: Turtle):
        car.color(choice(COLORS))

    def set_car(self, car: Turtle):
        """Changes the color and the position
        of the car.

        Args:
            car (Turtle): The car
        """
        self.set_car_color(car)
        self.set_car_position(car)
                
    def shift_cars(self):
        hidden_cars_indexes = self.get_hidden_cars_indexes()
                
        if len(hidden_cars_indexes) >= 1:
            for index in hidden_cars_indexes:
                car: Turtle = self.visible_cars[index]
                self.set_car(car)

                self.invisible_cars.append(car)
                self.visible_cars.pop(index)
                
    def collided_with_player(self, player: Turtle) -> bool:
        for car in self.visible_cars:
            if car.xcor() <= 20:
                if car.distance(player) < 20:
                    return True

    def increase_cars_speed(self):
        self.move_speed += MOVE_INCREMENT
