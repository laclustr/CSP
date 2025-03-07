import pygame
from CONSTS import *

class Board:
	def __init__(self, board):
		self.piece_list = board

	def _draw_vert_cols(self, surface):
		for col in range(len(self.piece_list[0]) + 2):
			if col != len(self.piece_list[0]) + 1:
				pygame.draw.line(
					surface,
					BLUE,
					(col * (DISPLAY_WIDTH // (len(self.piece_list[0]) + 1)), 0),
					(col * (DISPLAY_WIDTH // (len(self.piece_list[0]) + 1)), DISPLAY_HEIGHT),
					LINE_WIDTH
					)
			else:
				pygame.draw.line(
					surface,
					BLUE,
					(col * (DISPLAY_WIDTH // (len(self.piece_list[0]) + 1)) - LINE_WIDTH // 4, 0),
					(col * (DISPLAY_WIDTH // (len(self.piece_list[0]) + 1)) - LINE_WIDTH // 4, DISPLAY_HEIGHT),
					LINE_WIDTH
					)

	def _draw_horz_cols(self, surface):
		for row in range(len(self.piece_list[0]) + 2):
			if row != len(self.piece_list[0]) + 1:
				pygame.draw.line(
					surface,
					BLUE,
					(, 0),
					(0, 0),
					LINE_WIDTH
					)
			else:
				pygame.draw.line(
					surface,
					BLUE,
					(col * (DISPLAY_WIDTH // (len(self.piece_list[0]) + 1)) - LINE_WIDTH // 4, 0),
					(col * (DISPLAY_WIDTH // (len(self.piece_list[0]) + 1)) - LINE_WIDTH // 4, DISPLAY_HEIGHT),
					LINE_WIDTH
					)

	def check_win(self):
		sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		for row in self.piece_list:
			if sorted(row) != sorted_list:
				return False
		for col in range(len(self.piece_list[0])):
			curr_col = []
			for row in range(len(self.piece_list)):
				curr_col += [self.piece_list[row][col]]
			if sorted(curr_col) != sorted_list:
				return False
		for row in range(0, len(self.piece_list), 3):
			for col in range(0, len(self.piece_list[0]), 3):
				curr_3x3 = []
				for i in range(3):
					for j in range(3):
						curr_3x3 += [self.piece_list[row + i][col + j]]
				if sorted(curr_3x3) != sorted_list:
					return False
		return True

	def sudoku_valid_move(self, user_change):
		if len(user_change) != 4:
			return False
		if int(user_change[0]) not in range(1, len(puzzle) + 1):
			return False
		if int(user_change[1]) not in range(1, len(puzzle[0]) + 1):
			return False
		if int(user_change[3]) not in range(1, 10):
			return False
		return True

	def draw(self, surface):
		self._draw_vert_cols(surface)
		self._draw_horz_cols(surface)


		











