import pygame
from settings import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED,
    WHITE
)

class Paddle:
    """
    Represents a Paddle object used in the Pong game.

    Contains logic for moving paddles, resetting paddles to starting positions,
    and keeping track of player scores.

    Attributes:
        playernum (int): Indicates whether this paddle belongs to Player 1 or Player 2.
        score (int): The current score of the player.
        surf (pygame.Surface): The surface representing the paddle.
        rect (pygame.Rect): The rectangle defining the paddle's position and size.
        speed (int): The movement speed of the paddle.

    Methods:
        draw(screen): Draws the paddle on the game screen.
        update(dt): Updates the paddle's position based on user input.
        reset(): Resets the paddle to its initial position.
    """
    def __init__(self, playernum):
        """
        Initializes a Paddle object for the specified player.

        Args:
            playernum (int): Indicates the player (1 or 2). Determines the paddle's
            initial position and control keys.
        """
        self.playernum = playernum
        
        self.score = 0
        self.speed = PADDLE_SPEED
        self.surf = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect()

        self.reset()

    def draw(self, screen):
        """
        Draws the paddle on the game screen.

        Args:
            screen (pygame.Surface): The game screen where the paddle will be drawn.
        """
        screen.blit(self.surf, self.rect)

    def update(self, dt):
        """
        Updates the paddle's position based on user input and delta time.

        Args:
            dt (int): The time in milliseconds since the last frame, used to calculate
            movement with consistent speed across frames.

        TODO:
            - Handle user input to move the paddle up or down.
            - Implement delta time-based movement.
        """
        raise NotImplementedError

    def reset(self):
        """
        Resets the paddle to its starting position on the screen.
        Player 1's paddle starts on the left, while Player 2's paddle starts on the right.
        """
        if self.playernum == 1:
            self.rect.center = (30, SCREEN_HEIGHT // 2)
        else:
            self.rect.center = (SCREEN_WIDTH - 30, SCREEN_HEIGHT // 2)
