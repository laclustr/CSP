from CONSTS import *
import random
import pygame

class Mine:
    def __init__(self, is_mine):
        self.is_mine = is_mine
        self.is_flagged = False
        self.is_revealed = False
        self.surrounding_mines = 0

    def __repr__(self):
        return f"({self.is_mine}, {self.surrounding_mines})"

class Board:
    def __init__(self, n_rows, n_cols, n_mines):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.n_mines = n_mines
        self.n_flags = 0
        self.mines = self._generate_mines(n_rows, n_cols, n_mines)
        self.running = True
        self.game_start = False
        self.first_move = True
        self.lost = False
        self.elapsed_time = 0

    def __bool__(self):
        return self.running

    def _generate_mines(self, n_rows, n_cols, n_mines):
        mines = []
        for _ in range(n_mines):
            mines.append(Mine(True))
        for _ in range(n_rows * n_cols - n_mines):
            mines.append(Mine(False))

        random.shuffle(mines)
        new_mine_list = []
        for row in range(n_rows):
            new_row = []
            for col in range(n_cols):
                new_row.append(mines[row * n_cols + col])
            new_mine_list.append(new_row)
        return self._get_surrounding_mines(new_mine_list)

    def _get_surrounding_mines(self, mines):
        for row in range(len(mines)):
            for col in range(len(mines[0])):
                if not mines[row][col].is_mine:
                    counter = 0
                    if row > 0 and mines[row - 1][col].is_mine:
                        counter += 1
                    if row > 0 and col > 0 and mines[row - 1][col - 1].is_mine:
                        counter += 1
                    if row > 0 and col < len(mines[0]) - 1 and mines[row - 1][col + 1].is_mine:
                        counter += 1
                    if col > 0 and mines[row][col - 1].is_mine:
                        counter += 1
                    if col < len(mines[0]) - 1 and mines[row][col + 1].is_mine:
                        counter += 1
                    if row < len(mines) - 1 and mines[row + 1][col].is_mine:
                        counter += 1
                    if row < len(mines) - 1 and col > 0 and mines[row + 1][col - 1].is_mine:
                        counter += 1
                    if row < len(mines) - 1 and col < len(mines[0]) - 1 and mines[row + 1][col + 1].is_mine:
                        counter += 1
                    mines[row][col].surrounding_mines = counter
                else:
                    mines[row][col].surrounding_mines = -1
        return mines

    def _get_hovered_row_col(self, mouse_pos):
        cell_width = DISPLAY_WIDTH / self.n_cols
        cell_height = (DISPLAY_HEIGHT - DIST_FROM_TOP) / self.n_rows
        x, y = mouse_pos
        row = int((y - DIST_FROM_TOP) // cell_height)
        col = int(x // cell_width)
        if row < 0 or row >= self.n_rows or col < 0 or col >= self.n_cols:
            return None, None
        return row, col

    def _floodfill(self, row, col):
        to_be_checked = {(row, col)}

        while to_be_checked:
            current_row, current_col = to_be_checked.pop()

            if self.mines[current_row][current_col].is_revealed:
                continue
            self.mines[current_row][current_col].is_revealed = True

            if self.mines[current_row][current_col].surrounding_mines > 0:
                continue

            if current_row > 0 and not self.mines[current_row - 1][current_col].is_mine:
                to_be_checked.add((current_row - 1, current_col))
            if current_row < len(self.mines) - 1 and not self.mines[current_row + 1][current_col].is_mine:
                to_be_checked.add((current_row + 1, current_col))
            if current_col > 0 and not self.mines[current_row][current_col - 1].is_mine:
                to_be_checked.add((current_row, current_col - 1))
            if current_col < len(self.mines[0]) - 1 and not self.mines[current_row][current_col + 1].is_mine:
                to_be_checked.add((current_row, current_col + 1))
            if current_row > 0 and current_col > 0 and not self.mines[current_row - 1][current_col - 1].is_mine:
                to_be_checked.add((current_row - 1, current_col - 1))
            if current_row > 0 and current_col < len(self.mines[0]) - 1 and not self.mines[current_row - 1][
                current_col + 1].is_mine:
                to_be_checked.add((current_row - 1, current_col + 1))
            if current_row < len(self.mines) - 1 and current_col > 0 and not self.mines[current_row + 1][
                current_col - 1].is_mine:
                to_be_checked.add((current_row + 1, current_col - 1))
            if current_row < len(self.mines) - 1 and current_col < len(self.mines[0]) - 1 and not \
            self.mines[current_row + 1][current_col + 1].is_mine:
                to_be_checked.add((current_row + 1, current_col + 1))

    def reveal(self, mouse_pos):
        row, col = self._get_hovered_row_col(mouse_pos)
        if row is None or col is None:
            return

        mods = pygame.key.get_mods()
        if mods & pygame.KMOD_CTRL or mods & pygame.KMOD_META:
            self.flag(mouse_pos)
            return

        if not self.game_start:
            self.game_start = True

        if self.first_move:
            self.first_move = False
            while self.mines[row][col].is_mine or self._get_surrounding_mines(self.mines)[row][col].surrounding_mines != 0:
                self.mines = self._generate_mines(self.n_rows, self.n_cols, self.n_mines)
            self.mines = self._get_surrounding_mines(self.mines)

        if self.mines[row][col].is_mine:
            self.lost = True
            self._show_mines()
            return
        if self.mines[row][col].is_flagged or self.mines[row][col].is_revealed:
            return

        if self.mines[row][col].surrounding_mines == 0:
            self._floodfill(row, col)
        else:
            self.mines[row][col].is_revealed = True

    def flag(self, mouse_pos):
        row, col = self._get_hovered_row_col(mouse_pos)
        if row is None or col is None:
            return
        if not self.mines[row][col].is_revealed:
            if self.mines[row][col].is_flagged:
                self.n_flags -= 1
            else:
                self.n_flags += 1
            self.mines[row][col].is_flagged = not self.mines[row][col].is_flagged

    def win(self):
        all_non_mine_revealed = True
        for row in self.mines:
            for mine in row:
                if not mine.is_mine and not mine.is_revealed:
                    all_non_mine_revealed = False
                    break
            if not all_non_mine_revealed:
                break
        if all_non_mine_revealed:
            return True

        flagged_bombs = 0
        for row in self.mines:
            for mine in row:
                if mine.is_flagged:
                    if not mine.is_mine:
                        return False
                    flagged_bombs += 1
        return flagged_bombs == self.n_mines

    def loss(self):
        return self.lost

    def draw(self, screen):
        cell_width = DISPLAY_WIDTH / self.n_cols
        cell_height = (DISPLAY_HEIGHT - DIST_FROM_TOP) / self.n_rows
        font = pygame.font.Font(None, 36)

        for row in range(self.n_rows):
            for col in range(self.n_cols):
                mine = self.mines[row][col]
                x = col * cell_width
                y = row * cell_height + DIST_FROM_TOP

                if mine.is_flagged:
                    pygame.draw.rect(screen, PINK, (x, y, cell_width, cell_height))
                elif mine.is_revealed:
                    if not mine.is_mine:
                        color = WHITE if (row % 2 == col % 2) else DARK_WHITE
                        pygame.draw.rect(screen, color, (x, y, cell_width, cell_height))
                        if mine.surrounding_mines > 0:
                            text = font.render(str(mine.surrounding_mines), True, BLACK)
                            screen.blit(text, (x + cell_width / 2 - text.get_width() / 2, y + cell_height / 2 - text.get_height() / 2))
                    else:
                        pygame.draw.rect(screen, RED, (x, y, cell_width, cell_height))
                        pygame.draw.circle(screen, BLACK, (int(x + cell_width / 2), int(y + cell_height / 2)), 10)
                else:
                    color = LIGHT_BLUE if (row % 2 == col % 2) else DARK_BLUE
                    pygame.draw.rect(screen, color, (x, y, cell_width, cell_height))

        time_font = pygame.font.Font(None, WIN_FONT_SIZE)
        time_in_seconds = time_font.render(str(self.elapsed_time // 1000), True, BLACK)
        flags_left = time_font.render(str(self.n_mines - self.n_flags), True, BLACK)
        screen.blit(time_in_seconds, (DISPLAY_WIDTH - time_in_seconds.get_width() - 10, 10))
        screen.blit(flags_left, (10, 10))

    def _show_mines(self):
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                mine = self.mines[row][col]
                if mine.is_mine:
                    mine.is_revealed = True




if __name__ == "__main__":
    import os
    os.system("python3 main.py")

