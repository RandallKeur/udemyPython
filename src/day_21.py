""" Day 21 of Coding Challenges for fully implemented Snake"""
import time

from src.classes.snake_game import SnakeGame
from src.constants.values import SNAKE_SPEED


def snake() -> None:
    """Play a snake game"""
    snake_game = SnakeGame()
    speed = snake_game.screen.textinput(title="Snake Difficulty",
                                        prompt=f"How difficult do you want?"
                                               f"{SNAKE_SPEED.keys()}: ")
    snake_game.capture_keypress()

    while snake_game.on_map() and snake_game.no_collision():
        snake_game.screen.update()
        time.sleep(SNAKE_SPEED[speed])
        snake_game.snake.move()
        snake_game.eat_food()

    snake_game.screen.exitonclick()