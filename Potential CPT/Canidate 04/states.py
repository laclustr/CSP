from turtledemo.nim import SCREENWIDTH

import pygame
from sphinx.addnodes import centered

from CONSTS import *

settings = {
    "rows": N_ROWS,
    "cols": N_COLS,
    "mines": N_MINES
}

def draw_adjustment_menu(screen, board):
    screen.fill(GRAY)
    font = pygame.font.Font(None, WIN_FONT_SIZE)

    text = font.render("Adjust Settings", True, BLACK)
    text_rect = text.get_rect(center=(DISPLAY_WIDTH / 2, DIST_FROM_TOP / 2 + 5))
    screen.blit(text, text_rect)

    rows_text = font.render(f"Rows: {settings['rows']}", True, BLACK)
    cols_text = font.render(f"Columns: {settings['cols']}", True, BLACK)
    mine_text = font.render(f"Mines: {settings['mines']}", True, BLACK)
    start_text = font.render("Press Enter to Start", True, BLACK)
    start_rect = start_text.get_rect(center=(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2 + 150))

    screen.blit(rows_text, (50, DIST_FROM_TOP / 2 + 50))
    screen.blit(cols_text, (50, DIST_FROM_TOP / 2 + 100))
    screen.blit(mine_text, (50, DIST_FROM_TOP / 2 + 150))
    screen.blit(start_text, start_rect)

    if not settings["mines"] + 9 < settings["rows"] * settings["cols"]:
        start_text = font.render("Bomb Count too High!", True, RED)
        start_rect = start_text.get_rect(center=(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2 + 75))
        screen.blit(start_text, start_rect)

    plus_button = font.render("+", True, BLACK)
    minus_button = font.render("-", True, BLACK)

    for i, key in enumerate(["rows", "cols", "mines"]):
        y_pos = DIST_FROM_TOP / 2 + 50 + i * 50
        screen.blit(plus_button, (DISPLAY_WIDTH / 2 + 50, y_pos))
        screen.blit(minus_button, (DISPLAY_WIDTH / 2 + 100, y_pos))

def handle_adjustment_events(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos

        for i, key in enumerate(["rows", "cols", "mines"]):
            y_pos = DIST_FROM_TOP / 2 + 60 + i * 50

            if DISPLAY_WIDTH / 2 + 50 <= x <= DISPLAY_WIDTH / 2 + 70 and y_pos <= y <= y_pos + 30:
                settings[key] += 1

            elif DISPLAY_WIDTH / 2 + 100 <= x <= DISPLAY_WIDTH / 2 + 120 and y_pos <= y <= y_pos + 30:
                if settings[key] > 1:
                    settings[key] -= 1

def draw_won_menu(screen, board):
    screen.fill(GRAY)
    board.draw(screen)
    font = pygame.font.Font(None, WIN_FONT_SIZE)
    text = font.render("You Win!", True, BLACK)
    text_rect = text.get_rect(center=(DISPLAY_WIDTH / 2, DIST_FROM_TOP / 2 + 5))
    screen.blit(text, text_rect)

def draw_lost_menu(screen, board):
    screen.fill(GRAY)
    board.draw(screen)
    font = pygame.font.Font(None, WIN_FONT_SIZE)
    text = font.render("You Lose :(", True, BLACK)
    text_rect = text.get_rect(center=(DISPLAY_WIDTH / 2, DIST_FROM_TOP / 2 + 5))
    screen.blit(text, text_rect)

def draw_playing_menu(screen, board):
    screen.fill(GRAY)
    board.draw(screen)

if __name__ == "__main__":
    import os
    os.system("python3 main.py")