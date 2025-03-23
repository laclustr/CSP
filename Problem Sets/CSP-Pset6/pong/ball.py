import pygame
from settings import *

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

    def update(self, dt, paddles):
        self.rect.x += self.speed[0] * dt
        self.rect.y += self.speed[1] * dt

        if self.hit_wall():
            self.bounce("wall")

        if self.collides(paddles[0]):
            self.rect.left = paddles[0].rect.right
            self.bounce("paddle")
        elif self.collides(paddles[1]):
            self.rect.right = paddles[1].rect.left
            self.bounce("paddle")

    def bounce(self, obj):
        """
        Handles the logic for bouncing the ball off walls and paddles.

        Args:
            obj (str): Indicates what the ball collided with. Possible values are:
                - "wall": The ball hit a wall.
                - "paddle": The ball hit a paddle.

        Raises:
            ValueError: If the object is not "wall" or "paddle".

        """
        if obj not in {"wall", "paddle"}:
            raise ValueError("Ball can only bounce off walls and paddles.")
        if obj == "wall":
            self.speed[1] = -self.speed[1]
            WALL_SOUND.play()
        elif obj == "paddle":
            self.speed[0] = -self.speed[0] * (SPEED_INCREASE + 1)
            self.speed[1] *= (SPEED_INCREASE + 1)
            if self.speed[0] > MAX_BALL_SPEED:
                self.speed[0] = MAX_BALL_SPEED
            if self.speed[1] > MAX_BALL_SPEED:
                self.speed[1] = MAX_BALL_SPEED
            PADDLE_SOUND.play()

    def collides(self, other):
        """
        Checks if the ball collides with another object, typically a paddle.

        Args:
            other (Paddle): The paddle to check for a collision.

        Returns:
            bool: True if the ball collides with the paddle, False otherwise.

        """
        return self.rect.colliderect(other.rect)

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

        """
        return self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT

    def point_scored(self):
        """
        Determines if a player has scored a point.

        Returns:
            int: 
                -1 if Player 2 scores a point.
                 1 if Player 1 scores a point.
                 0 if the ball is still in play and no point has been scored.
        """
        if self.rect.left < 0:
            SCORE_SOUND.play()
            return -1
        if self.rect.right > SCREEN_WIDTH:
            SCORE_SOUND.play()
            return 1
        return 0

    def set_speed(self, xval=None, yval=None):
        if not (xval and yval):
            return
        if xval:
            self.speed[0] = xval
        if yval:
            self.speed[1] = yval