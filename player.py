from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
NORTH = 90


class Player(Turtle):
    def __init__(self, shape: str = "turtle", ) -> None:
        super().__init__(shape)
        
        self.penup()
        self.setheading(NORTH)
        self.setpos(STARTING_POSITION)

    def next_level(self):
        self.setpos(STARTING_POSITION)

    def in_finish_line(self) -> bool:
        if self.ycor() >= FINISH_LINE_Y:
            return True

    def up(self):
        self.forward(MOVE_DISTANCE)
