import pygame
import time

def main():
	pygame.init()
	flags = pygame.RESIZABLE | pygame.NOFRAME
	pygame.display.set_mode(size=(1920, 1080), flags=flags)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return
		time.sleep(1)

if __name__ == "__main__":
	main()