import pygame
from CONSTS import *
from states import *
from game import Board

def main():
    pygame.init()
    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("Minesweeper")

    clock = pygame.time.Clock()
    running = True
    board = Board(N_ROWS, N_COLS, N_MINES)
    font = pygame.font.Font(None, WIN_FONT_SIZE)

    game_state = "adjust"

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_state == "playing":
                    if event.button == 1:
                        board.reveal(event.pos)
                    elif event.button == 3:
                        board.flag(event.pos)

                if game_state == "won" or game_state == "lost":
                    game_state = "adjust"

                if game_state == "adjust":
                    handle_adjustment_events(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and game_state == "adjust":
                    if settings["rows"] > 0 and settings["cols"] > 0 and settings["mines"] > 0 and settings["mines"] + 9 < settings["rows"] * settings["cols"]:
                        board = Board(settings["rows"], settings["cols"], settings["mines"])
                        game_state = "playing"

        dt = clock.tick(FPS)
        if board.running and board.game_start:
            board.elapsed_time += dt

        if game_state == "playing" and board.win():
            game_state = "won"
            board.running = False
        if game_state == "playing" and board.loss():
            game_state = "lost"
            board.running = False

        if game_state == "won":
            draw_won_menu(screen, board)
            pygame.display.flip()

        if game_state == "lost":
            draw_lost_menu(screen, board)
            pygame.display.flip()

        if game_state == "adjust":
            draw_adjustment_menu(screen, board)
            pygame.display.flip()

        elif game_state == "playing":
            draw_playing_menu(screen, board)
            pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit()
