"""
This is a game I'd like to make in order to help practice learning
new languages. It'll feature some sort of game element and allow
users to input custom word lists they'd like to work on. Idk yet,
but I hope it works.
"""
VERSION = "0.01"

try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from datetime import datetime
    from socket import *
    from pygame.locals import *
except (ImportError, err):
    print(f"couldn't load module. {err}")
    sys.exit(2)

def main():
	pygame.init()
	pygame.font.init()
	flags = pygame.RESIZABLE
	screen = pygame.display.set_mode((680, 440), flags=flags, vsync=1)
	pygame.display.set_caption("Translator Game")
	
	start_time = datetime.now()
	clock = pygame.time.Clock()

	color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
	curr_color_idx = 0

	rect = pygame.Rect(20, 20, 640, 40)
	rect_color = "black"
	font = pygame.font.SysFont("arialrounded", 40)

	running = True
	while running:
		screen.fill(color_list[curr_color_idx])
		pygame.draw.rect(screen, rect_color, rect)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		keys = pygame.key.get_pressed()
		mouse_pressed = pygame.mouse.get_pressed(num_buttons=3)
		mouse_pos = pygame.mouse.get_pos()
		rect_hover = mouse_pos[0] in range(rect.left, rect.left + rect.width + 1) and mouse_pos[1] in range(rect.top, rect.top + rect.height + 1)

		if rect_hover and mouse_pressed[0]:
			rect_color = "orange"
			screen.blit(font.render("Button Pressed!", False, (255, 255, 255)), (rect.x + 10, rect.y + 7))
		elif rect_hover:
			rect_color = "gray"
			screen.blit(font.render("Button Hovered!", False, (255, 255, 255)), (rect.x + 10, rect.y + 7))
		else:
			rect_color = "black"
			screen.blit(font.render("Button!", False, (255, 255, 255)), (rect.x + 10, rect.y + 7))

		window_size = pygame.display.get_window_size()
		if rect.left > window_size[0]:
			rect.left = 0
		if rect.top > window_size[1]:
			rect.top = 0
		if rect.left < 0:
			rect.left = window_size[0]
		if rect.top < 0:
			rect.top = window_size[1]

		pygame.display.flip()
		clock.tick(60)

	pygame.quit()




if __name__ == "__main__": main()



























