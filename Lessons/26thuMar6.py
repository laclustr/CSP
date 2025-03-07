import pygame
import math

pygame.init()

display = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

class Player:
	def __init__(self, pos, size, color=(255, 17, 255)):
		self.surf = pygame.Surface((size, size), pygame.DOUBLEBUF | pygame.HWSURFACE)
		self.rect = self.surf.get_rect(center=pos)
		self.surf.fill(color)
		self.speed = 0.5
		self.color = color

	def draw(self, display):
		display.blit(self.surf, self.rect)

	def move(self, dt):
		keys = pygame.key.get_pressed()
		movement = [0, 0]

		if keys[pygame.K_w]:
			movement[1] = -1
		if keys[pygame.K_s]:
			movement[1] = 1
		if keys[pygame.K_a]:
			movement[0] = -1
		if keys[pygame.K_d]:
			movement[0] = 1

		if movement[0] != 0 and movement[1] != 0:
			movement[0] /= 2**0.5
			movement[1] /= 2**0.5

		self.rect.x += movement[0] * dt * self.speed
		self.rect.y += movement[1] * dt * self.speed

		self.rect.left = max(self.rect.left, 0)
		self.rect.right = min(self.rect.right, 640)
		self.rect.top = max(self.rect.top, 0)
		self.rect.bottom = min(self.rect.bottom, 480)

def draw_mouse_dot(display):
	pygame.draw.circle(display, (192, 12, 33), pygame.mouse.get_pos(), 9)

def draw_aim_line(display, player):
	mouse_pos = pygame.mouse.get_pos()
	origin = player.rect.center
	dy = mouse_pos[1] - origin[1]
	dx = mouse_pos[0] - origin[0]
	r = 64

	theta = math.atan2(dy, dx)

	end_pos = [origin[0] + r * math.cos(theta), origin[1] + r * math.sin(theta)]

	pygame.draw.line(display, player.color, origin, end_pos, width=12)

player = Player((320, 240), 28)

running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	dt = clock.tick(60)
	player.move(dt)
	display.fill((255, 255, 255))
	player.draw(display)
	draw_mouse_dot(display)
	draw_aim_line(display, player)

	pygame.display.flip()

pygame.quit()