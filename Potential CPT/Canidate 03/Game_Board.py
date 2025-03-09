import pygame
from CONSTS import *

class Board:
	def __init__(self, board, sel_idx=(0,0)):
		self.piece_list = [[0 for _ in row] for row in board]
		self.og_piece_list = [row[:] for row in board]
		self.sel_idx = sel_idx

	def _draw_sel_square(self, surface):
		rect = pygame.Rect(
			self.sel_idx[1] * (DISPLAY_WIDTH // len(self.piece_list[0])),
			self.sel_idx[0] * (DISPLAY_HEIGHT // len(self.piece_list)),
			DISPLAY_WIDTH // len(self.piece_list[0]),
			DISPLAY_HEIGHT // len(self.piece_list)
			)
		pygame.draw.rect(surface, RED, rect)

	def _draw_vert_cols(self, surface):
		for col in range(len(self.piece_list[0]) + 1):
			if col % 3 != 0 or col == 0:
				pygame.draw.line(
					surface,
					DARK_BLUE,
					(col * (DISPLAY_WIDTH // len(self.piece_list[0])), 0),
					(col * (DISPLAY_WIDTH // len(self.piece_list[0])), DISPLAY_HEIGHT),
					LINE_WIDTH
					)
			elif col == len(self.piece_list[0]):
				pygame.draw.line(
					surface,
					DARK_BLUE,
					(col * (DISPLAY_WIDTH // len(self.piece_list[0])) - LINE_WIDTH // 4, 0),
					(col * (DISPLAY_WIDTH // len(self.piece_list[0])) - LINE_WIDTH // 4, DISPLAY_HEIGHT),
					LINE_WIDTH
					)

	def _draw_horz_cols(self, surface):
		for row in range(len(self.piece_list) + 1):
			if row % 3 != 0 or row == 0:
				pygame.draw.line(
					surface,
					DARK_BLUE,
					(0, row * (DISPLAY_HEIGHT // len(self.piece_list))),
					(DISPLAY_WIDTH, row * (DISPLAY_HEIGHT // len(self.piece_list))),
					LINE_WIDTH
					)
			elif row == len(self.piece_list):
				pygame.draw.line(
					surface,
					DARK_BLUE,
					(0, row * (DISPLAY_HEIGHT // len(self.piece_list)) - LINE_WIDTH // 4),
					(DISPLAY_WIDTH, row * (DISPLAY_HEIGHT // len(self.piece_list)) - LINE_WIDTH // 4),
					LINE_WIDTH
					)

	def _draw_separators(self, surface):
		for row in range(len(self.piece_list) + 1):
			if row % 3 == 0 and row != 0 and row != len(self.piece_list):
				pygame.draw.line(
					surface,
					PINK,
					(0, row * (DISPLAY_HEIGHT // len(self.piece_list))),
					(DISPLAY_WIDTH, row * (DISPLAY_HEIGHT // len(self.piece_list))),
					LINE_WIDTH
					)

		for col in range(len(self.piece_list[0]) + 1):
			if col % 3 == 0 and col != 0 and col != len(self.piece_list[0]):
				pygame.draw.line(
					surface,
					PINK,
					(col * (DISPLAY_WIDTH // len(self.piece_list[0])), 0),
					(col * (DISPLAY_WIDTH // len(self.piece_list[0])), DISPLAY_HEIGHT),
					LINE_WIDTH
					)

	def _draw_numbers(self, surface):
		for row in range(len(self.og_piece_list)):
			for col in range(len(self.og_piece_list[0])):
				if self.og_piece_list[row][col] != 0:
					font = pygame.font.Font(None, 36)
					text = font.render(str(self.og_piece_list[row][col]), True, BLACK)
					text_rect = text.get_rect(center=(
						col * (DISPLAY_WIDTH // len(self.og_piece_list[0])) + (DISPLAY_WIDTH // len(self.og_piece_list[0]) // 2),
						row * (DISPLAY_HEIGHT // len(self.og_piece_list)) + (DISPLAY_HEIGHT // len(self.og_piece_list) // 2))
					)
					surface.blit(text, text_rect)

		for row in range(len(self.piece_list)):
			for col in range(len(self.piece_list[0])):
				if self.piece_list[row][col] != 0 and not self.og_piece_list[row][col]:
					font = pygame.font.Font(None, 36)
					text = font.render(str(self.piece_list[row][col]), True, WHITE)
					text_rect = text.get_rect(center=(
						col * (DISPLAY_WIDTH // len(self.piece_list[0])) + (DISPLAY_WIDTH // len(self.piece_list[0]) // 2),
						row * (DISPLAY_HEIGHT // len(self.piece_list)) + (DISPLAY_HEIGHT // len(self.piece_list) // 2))
					)
					surface.blit(text, text_rect)


	def win(self):
		check_list = [
			[a if a != 0 else b for a, b in zip(main_row, secondary_row)]
			for main_row, secondary_row in zip(self.og_piece_list, self.piece_list)
		]
		sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		for row in check_list:
			if sorted(row) != sorted_list:
				return False
		for col in range(len(check_list[0])):
			curr_col = []
			for row in range(len(check_list)):
				curr_col += [check_list[row][col]]
			if sorted(curr_col) != sorted_list:
				return False
		for row in range(0, len(check_list), 3):
			for col in range(0, len(check_list[0]), 3):
				curr_3x3 = []
				for i in range(3):
					for j in range(3):
						curr_3x3 += [check_list[row + i][col + j]]
				if sorted(curr_3x3) != sorted_list:
					return False
		return True

	def draw(self, surface):
		self._draw_sel_square(surface)
		self._draw_vert_cols(surface)
		self._draw_horz_cols(surface)
		self._draw_separators(surface)
		self._draw_numbers(surface)

	def move(self, keys):
		if keys[pygame.K_UP]:
			self.sel_idx = (self.sel_idx[0] - 1, self.sel_idx[1])
		if keys[pygame.K_DOWN]:
			self.sel_idx = (self.sel_idx[0] + 1, self.sel_idx[1])
		if keys[pygame.K_LEFT]:
			self.sel_idx = (self.sel_idx[0], self.sel_idx[1] - 1)
		if keys[pygame.K_RIGHT]:
			self.sel_idx = (self.sel_idx[0], self.sel_idx[1] + 1)
		self.sel_idx = (max(0, min(len(self.piece_list) - 1, self.sel_idx[0])), max(0, min(len(self.piece_list[0]) - 1, self.sel_idx[1])))

	def set_num(self, keys):
		if keys[pygame.K_1]:
			self.piece_list[self.sel_idx[0]][self.sel_idx[1]] = 1
		elif keys[pygame.K_2]:
			self.piece_list[self.sel_idx[0]][self.sel_idx[1]] = 2
		elif keys[pygame.K_3]:
			self.piece_list[self.sel_idx[0]][self.sel_idx[1]] = 3
		elif keys[pygame.K_4]:
			self.piece_list[self.sel_idx[0]][self.sel_idx[1]] = 4
		elif keys[pygame.K_5]:
			self.piece_list[self.sel_idx[0]][self.sel_idx[1]] = 5
		elif keys[pygame.K_6]:
			self.piece_list[self.sel_idx[0]][self.sel_idx[1]] = 6
		elif keys[pygame.K_7]:
			self.piece_list[self.sel_idx[0]][self.sel_idx[1]] = 7
		elif keys[pygame.K_8]:
			self.piece_list[self.sel_idx[0]][self.sel_idx[1]] = 8
		elif keys[pygame.K_9]:
			self.piece_list[self.sel_idx[0]][self.sel_idx[1]] = 9
		elif keys[pygame.K_BACKSPACE]:
			self.piece_list[self.sel_idx[0]][self.sel_idx[1]] = 0

if __name__ == "__main__":
	import os
	os.system("python3 main.py")












