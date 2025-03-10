from ball import Ball
from gamefont import GameFont
from paddle import Paddle
import pygame
from settings import (
	GRAY, WHITE,
	SCREEN_WIDTH, SCREEN_HEIGHT
)

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("P0NG")

font = GameFont("font.ttf", WHITE)
font.add_size("score", 84)

player1 = Paddle(1)
player2 = Paddle(2)
ball    = Ball()

curr_server = "Player1"

state = "serve"

running = True
while running:
	keydown_keys = set()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			keydown_keys.add(event.key)

	dt = clock.tick(60)

	if state == "welcome":
		"""
			TODO:
		"""
		pass
	elif state == "serve":
		screen.fill(GRAY)
		font.set_size("score")
		font.print(screen, str(player1.score), SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
		font.print(screen, str(player2.score), 3 * SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)

		font.set_size("medium")
		font.print(screen, f"{curr_server} is serving.", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5)
		font.print(screen, f"Press ENTER to serve...", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5 + font.get_size())

		player1.draw(screen)
		player2.draw(screen)
		ball.draw(screen)
	elif state == "pause":
		"""
			TODO:
		"""
		pass
	elif state == "play":
		"""
			TODO:
		"""
		pass
	elif state == "gameover":
		"""
			TODO:
		"""
		pass

	pygame.display.flip()

pygame.quit()