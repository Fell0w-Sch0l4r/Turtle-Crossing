from time import sleep
from turtle import Screen
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
    sleep(cars.playtime)
    screen.update()
    
    cars.move_cars()
    
    if cars.collided_with_player(player):
        score_board.game_over()
        break
    
    if player.in_finish_line():
        player.next_level()
        score_board.increase_level()
        cars.increase_cars_speed()


screen.exitonclick()
