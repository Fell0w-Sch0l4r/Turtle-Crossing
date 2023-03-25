import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score_board = Scoreboard()

cars = CarManager()

screen.listen()
screen.onkey(key="Up", fun=player.up)


while True:
    time.sleep(0.1)
    screen.update()
    
    cars.move_cars()
    
    if cars.colided_with_player(player):
        score_board.game_over()
        break
    
    if player.in_finish_line():
        player.next_level()
        score_board.increase_level()


screen.exitonclick()


