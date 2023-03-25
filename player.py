from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape: str = "turtle", ) -> None:
        super().__init__(shape)
        
        self.penup()
        self.setheading(90)
        self.setpos(STARTING_POSITION)
        
        
    def up(self):
        new_y: float = self.ycor() + MOVE_DISTANCE
        self.sety(new_y)
