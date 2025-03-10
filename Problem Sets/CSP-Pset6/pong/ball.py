import pygame
from settings import (
    BALL_SIZE, BALL_SPEED_X, BALL_SPEED_Y, SPEED_INCREASE,
    SCREEN_HEIGHT, SCREEN_WIDTH,
    WHITE
)

class Ball:
    """
    Represents a ball in the Pong game.

    The ball can collide with walls or paddles, and its behavior is defined
    through various methods.

    Attributes:
        surf (pygame.Surface): The surface representing the ball.
        rect (pygame.Rect): The rectangle defining the ball's position and size.
        speed (list[int, int]): The ball's x and y speed components.

    Methods:
        reset(): Resets the ball's position to the center and randomizes its velocity.
        bounce(obj): Handles bouncing when the ball hits a wall or paddle.
        collides(other): Checks for a collision with a paddle.
        draw(screen): Draws the ball on the game screen.
        hit_wall(): Checks if the ball has hit the top or bottom walls.
        point_scored(): Determines if a point has been scored.
    """

    def __init__(self):
        """
        Initializes the Ball with a surface, a rectangle, and initial speed.

        The surface and rectangle are defined using constants imported from
        the settings module. The ball's position and speed are initialized
        using the reset() method.
        """
        self.surf = pygame.Surface((BALL_SIZE, BALL_SIZE))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect()

        self.speed = [BALL_SPEED_X, BALL_SPEED_Y]
        self.reset()

    def reset(self):
        """
        Resets the ball's position to the center of the screen.

        The x and y velocities of the ball are also randomized to introduce
        variability in gameplay.
        """
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def bounce(self, obj):
        """
        Handles the logic for bouncing the ball off walls and paddles.

        Args:
            obj (str): Indicates what the ball collided with. Possible values are:
                - "wall": The ball hit a wall.
                - "paddle": The ball hit a paddle.

        Raises:
            ValueError: If the object is not "wall" or "paddle".

        TODO:
            Implement the actual bouncing logic.
        """
        if obj not in {"wall", "paddle"}:
            raise ValueError("Ball can only bounce off walls and paddles.")
        if obj == "wall":
            pass  # Logic for bouncing off walls goes here.
        elif obj == "paddle":
            pass  # Logic for bouncing off paddles goes here.

        raise NotImplementedError()

    def collides(self, other):
        """
        Checks if the ball collides with another object, typically a paddle.

        Args:
            other (Paddle): The paddle to check for a collision.

        Returns:
            bool: True if the ball collides with the paddle, False otherwise.

        TODO:
            Implement collision detection logic.
        """
        raise NotImplementedError()

    def draw(self, screen):
        """
        Draws the ball on the game screen.

        Args:
            screen (pygame.Surface): The game screen where the ball will be drawn.
        """
        screen.blit(self.surf, self.rect)

    def hit_wall(self):
        """
        Checks if the ball hits the top or bottom walls of the screen.

        Returns:
            bool: True if the ball hits the top or bottom walls, False otherwise.

        TODO:
            Implement wall collision detection logic.
        """
        raise NotImplementedError()

    def point_scored(self):
        """
        Determines if a player has scored a point.

        Returns:
            int: 
                -1 if Player 2 scores a point.
                 1 if Player 1 scores a point.
                 0 if the ball is still in play and no point has been scored.

        TODO:
            Implement point-scoring logic.
        """
        raise NotImplementedError()