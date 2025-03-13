import random
import pygame
from powerup import PowerUp, use_powerup
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
ai      = False

all_powerups = [
	PowerUp("ball_speed_mul", 0.5),
	PowerUp("ball_speed_mul", 1.5),
	PowerUp("paddle_size", 1.5),
	PowerUp("paddle_size", 0.4),
	PowerUp("paddle_speed", 0.75),
	PowerUp("paddle_speed", 1.5)
]
active_powerups = []

welcome_selector = True
curr_server = "Player 1"

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

		font.set_color(BLUE)
		if welcome_selector:
			font.print(screen, "1 PLAYER", SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2, True)
			font.set_color(WHITE)
			font.print(screen, "2 PLAYER", SCREEN_WIDTH - SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2, True)

		if not welcome_selector:
			font.print(screen, "2 PLAYER", SCREEN_WIDTH - SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2, True)
			font.set_color(WHITE)
			font.print(screen, "1 PLAYER", SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2, True)

		if pygame.K_RETURN in keydown_keys:
			state = "serve"
			ai = welcome_selector

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

		player1.update(dt, ai, ball)
		player2.update(dt, ai, ball)

		if pygame.K_RETURN in keydown_keys:
			randspeed = random.uniform(-BALL_RAND_SPEED_Y, BALL_RAND_SPEED_Y)
			randspeed += 1 if randspeed >= 0 else -1
			if curr_server == "Player 1":
				ball.speed = [BALL_SPEED_X * abs(randspeed), BALL_SPEED_Y * randspeed]
			elif curr_server == "Player 2":
				ball.speed = [-BALL_SPEED_X * abs(randspeed), BALL_SPEED_Y * randspeed]
			state = "play"

	elif state == "pause":
		screen.fill(GRAY)
		player1.draw(screen)
		player2.draw(screen)
		ball.draw(screen)

		font.set_size("medium")
		font.set_color(WHITE)
		font.print(screen, f"Paused", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5)
		font.print(screen, f"Press \"p\" to continue playing.", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5 + font.get_size())

		if pygame.K_p in keydown_keys:
			state = "play"

	elif state == "play":
		screen.fill(GRAY)

		ball.update(dt, [player1, player2])
		player1.update(dt, ai, ball)
		player2.update(dt, ai, ball)

		if use_powerup(active_powerups):
			pwrcopy = random.choice(all_powerups)
			power = PowerUp(pwrcopy.power_type, pwrcopy.num)
			active_powerups.append(power)
			power.visible = True

		for power in active_powerups.copy():
			power.draw(screen, dt)
			if not power.visible and not power.applied:
				active_powerups.remove(power)
				continue
			elif power.visible:
				if ball.collides(power):
					res = power.apply(ball, [player1, player2])
					ball, [player1, player2] = res
			if power.time_remaining <= 0:
				same_types = []
				for pwr in active_powerups:
					if pwr.power_type == power.power_type and id(power) != id(pwr) and pwr.time_remaining > 0:
						same_types.append(pwr)
				if len(same_types) == 0:
					res = power.remove(ball, [player1, player2])
					if res:
						ball, [player1, player2] = res
				active_powerups.remove(power)

		match ball.point_scored():
			case -1:
				player2.score += 1
				for power in active_powerups:
					res = power.remove(ball, [player1, player2], True)
					if res:
						ball, [player1, player2] = res
				active_powerups = []
				ball.reset()
				player1 = Paddle(1)
				player2 = Paddle(2)
				curr_server = "Player 2" if curr_server == "Player 1" else "Player 1"
				state = "serve"
			case 1:
				player1.score += 1
				for power in active_powerups:
					res = power.remove(ball, [player1, player2], True)
					if res:
						ball, [player1, player2] = res
				active_powerups = []
				ball.reset()
				player1 = Paddle(1)
				player2 = Paddle(2)
				curr_server = "Player 2" if curr_server == "Player 1" else "Player 1"
				state = "serve"

		player1.draw(screen)
		player2.draw(screen)
		ball.draw(screen)

		if pygame.K_p in keydown_keys:
			state = "pause"
		if player1.win() or player2.win():
			state = "gameover"

	elif state == "gameover":
		win_num = player1.playernum if player1.win() else player2.playernum
		screen.fill(GRAY)
		font.set_size("score")
		font.set_color(WHITE)
		font.print(screen, f"Game Over", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5)
		font.print(screen, f"Player {win_num} Wins!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5 + font.get_size())
		dist = font.get_size() * 2
		font.set_size("medium")
		font.print(screen, f"Press Enter to Play Again", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5 + dist)

		if pygame.K_RETURN in keydown_keys:
			player1 = Paddle(1)
			player2 = Paddle(2)
			curr_server = "Player 1"
			state = "welcome"

	pygame.display.flip()

pygame.quit()