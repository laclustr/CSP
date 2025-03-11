import random
import pygame

from ball import Ball
from gamefont import GameFont
from paddle import Paddle
from settings import *

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PONG")

font = GameFont("font.ttf", WHITE)
font.add_size("score", 84)

player1 = Paddle(1)
player2 = Paddle(2)
ball    = Ball()
ai = False

welcome_selector = True
curr_server = "Player1"

state = "welcome"

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
		screen.fill(GRAY)
		font.set_size("large")
		font.set_color(WHITE)
		font.print(screen, "P0NG", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4, True)
		if pygame.K_LEFT in keydown_keys:
			welcome_selector = True
		elif pygame.K_RIGHT in keydown_keys:
			welcome_selector = False
		if welcome_selector:
			font.set_color(BLUE)
			font.print(screen, "1 PLAYER", SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2, True)
			font.set_color(WHITE)
			font.print(screen, "2 PLAYER", SCREEN_WIDTH - SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2, True)

		if not welcome_selector:
			font.set_color(BLUE)
			font.print(screen, "2 PLAYER", SCREEN_WIDTH - SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2, True)
			font.set_color(WHITE)
			font.print(screen, "1 PLAYER", SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2, True)

		if pygame.K_RETURN in keydown_keys:
			state = "serve"
			ai = not welcome_selector


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

		player1.update(dt)
		player2.update(dt)

		if pygame.K_RETURN in keydown_keys:
			ball.speed = [BALL_SPEED_X, -BALL_SPEED_Y]
			state = "play"

	elif state == "pause":
		"""
			TODO:
		"""
		pass
	elif state == "play":
		screen.fill(GRAY)

		player1.update(dt)
		player2.update(dt)
		ball.update(dt, [player1, player2])

		match ball.point_scored():
			case -1:
				player2.score += 1
				state = "serve"
			case 1:
				player2.score += 1
				ball.reset()
				state = "serve"
			case 0:
				pass

		player1.draw(screen)
		player2.draw(screen)
		ball.draw(screen)
	elif state == "gameover":
		"""
			TODO:
		"""
		pass

	pygame.display.flip()

pygame.quit()