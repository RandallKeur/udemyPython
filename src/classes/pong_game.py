"""Class for the pong game"""
from turtle import Screen

from src.classes.pong_ball import PongBall
from src.classes.pong_scoreboard import PongScoreboard
from src.classes.pong_paddle import PongPaddle
from src.constants.values import PONG_SCREEN_SIZE, PONG_PADDLE_LOCATION, PONG_SCREEN, PONG_OFFSETS


class PongGame:
    """Class for the pong game"""

    def __init__(self):
        self.screen = Screen()
        self.setup_screen()
        self.scoreboard = PongScoreboard()
        self.left_paddle = PongPaddle(PONG_PADDLE_LOCATION["left"])
        self.right_paddle = PongPaddle(PONG_PADDLE_LOCATION["right"])
        self.ball = PongBall()

    def setup_screen(self):
        """Set up the screen for the pong game"""
        self.screen = Screen()
        self.screen.setup(width=PONG_SCREEN_SIZE["x"], height=PONG_SCREEN_SIZE["y"])
        self.screen.bgcolor("black")
        self.screen.title("Pong")
        self.screen.tracer(0)

    def capture_keypress(self):
        """Capture the key pressed and move the paddle"""
        self.screen.listen()
        self.screen.onkey(key="Up", fun=self.right_paddle.move_up)
        self.screen.onkey(key="Down", fun=self.right_paddle.move_down)
        self.screen.onkey(key="r", fun=self.left_paddle.move_up)
        self.screen.onkey(key="f", fun=self.left_paddle.move_down)

    def detect_collision_with_paddle(self):
        if self.right_paddle.ycor() - 50 <= self.ball.ycor() <= self.right_paddle.ycor() + 50 \
                and self.ball.xcor() > PONG_PADDLE_LOCATION["right"] - PONG_OFFSETS["paddle"] \
                or self.ball.distance(self.left_paddle) < 50 \
                and self.ball.xcor() < PONG_PADDLE_LOCATION["left"] + PONG_OFFSETS["paddle"]:
            self.ball.bounce()

    def detect_collision_with_wall(self):
        if self.ball.ycor() > PONG_SCREEN["y"]["max"] - PONG_OFFSETS["ball"] \
                or self.ball.ycor() < PONG_SCREEN["y"]["min"] + PONG_OFFSETS["ball"]:
            self.ball.bounce()
            
    def detect_collisions(self):
        self.detect_collision_with_paddle()
        self.detect_collision_with_wall()

    def score_left(self):
        self.scoreboard.score["left"] += 1
        self.scoreboard.update_scoreboard()
        self.ball.reset_position()

    def score_right(self):
        self.scoreboard.score["right"] += 1
        self.scoreboard.update_scoreboard()
        self.ball.reset_position()
    
    def detect_goal(self):
        if self.ball.xcor() > PONG_PADDLE_LOCATION["right"]:
            self.score_left()
        if self.ball.xcor() < PONG_PADDLE_LOCATION["left"]:
            self.score_right()
