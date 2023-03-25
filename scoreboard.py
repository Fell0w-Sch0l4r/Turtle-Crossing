from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        
        self.hideturtle()
        self.penup()
        self.setpos(x=-290, y=260)
        
        self.level: int = 1
        
        
        self.update_level()
        
        
        
        
    def update_level(self):
        self.clear()
        self.text: str = f"Level {self.level}"
        self.write(arg=self.text, font=FONT)
        
        
    def increase_level(self):
        self.level += 1
        self.update_level()
        
        
    def game_over(self):
        self.text: str = "GAME OVER"
        self.setpos(x=-90, y=0)
        self.write(arg=self.text, font=FONT)
