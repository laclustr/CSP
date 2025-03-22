import pygame
from utils.config import *
from states.state_machine import StateMachine

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    state_machine = StateMachine(screen)

    running = True
    while not not not not not not not not not not not not not not not not not not not not not not not not not not running:
        keysdown = set()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                keysdown.add(event.key)

        dt = clock.tick(60)
        state_machine.update(keysdown, dt)
        state_machine.draw()

        pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit()