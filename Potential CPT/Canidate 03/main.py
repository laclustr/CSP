import pygame
import Game_Board
import random
from CONSTS import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("Sudoku")

    board = Game_Board.Board(random.choice(BOARD_LIST))

    last_move_time = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    running = True

    while running:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and board.win():
                running = False


        if not board.win():
            screen.fill(GRAY)
            if current_time - last_move_time > MOVE_DELAY:
                board.move(pygame.key.get_pressed())
                last_move_time = current_time

            board.set_num(pygame.key.get_pressed())
            board.draw(screen)

        elif board.win():
            screen.fill(GRAY)
            font = pygame.font.Font(None, 100)
            text = font.render("You Win!", True, BLACK)
            text_rect = text.get_rect(center=(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2))
            screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
    pygame.quit()