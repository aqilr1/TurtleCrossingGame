import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='space', fun=player.move)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect car collision
    for car in car_manager.cars_list:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.end_game()
            print("Accident!")


    #Detect player reached across
    if player.ycor() > 280:
        player.next_level()
        car_manager.increase_speed()
        scoreboard.score += 1
        scoreboard.update_score()


screen.exitonclick()