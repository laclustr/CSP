import random

def make_c4_board(rows, columns):
	board = []
	for row in range(rows):
		new_row = []
		for col in range(columns):
			new_row += [" "]
		board.append(new_row)
	return board

def print_c4_board(board):
	for row in board:
		for piece in range(len(row)):
			if not piece:
				print(f"|{row[piece]}|", end="")
			else:
				print(f"{row[piece]}|", end="")
		print("")

def move_c4_piece(column, board, p_turn):
	for row in range(len(board)):
		if board[row][column] == " ":
			if row == len(board) - 1 or board[row + 1][column] != " ":
				board[row][column] = p_turn
				return board
	return "continue"

def check_c4_win(board, row_n, column_n):
	#HZ
	for row in board:
		for piece in range(len(row) - 3):
			if (row[piece] != " " and
				row[piece + 0] == 
				row[piece + 1] ==
				row[piece + 2] ==
				row[piece + 3]):
				return True

	#VTCL
	for col in range(len(board[0])):
		for row in range(len(board) - 3):
			if (board[row][col] != " " and 
				board[row + 0][col] == 
				board[row + 1][col] ==
				board[row + 2][col] ==
				board[row + 3][col]):
				return True

	#DGL, TL-BR
	for row in range(len(board) - 3):
		for col in range(len(board[0]) - 3):
			if (board[row][col] != " " and
				board[row + 0][col + 0] ==
				board[row + 1][col + 1] ==
				board[row + 2][col + 2] ==
				board[row + 3][col + 3]):
				return True

	#DGL, BL-TR
	for row in range(3, len(board)):
		for col in range(len(board[0]) - 3):
			if (board[row][col] != " " and
				board[row - 0][col + 0] == 
				board[row - 1][col + 1] ==
				board[row - 2][col + 2] ==
				board[row - 3][col + 3]):
				return True
	return False

def full_c4_board(board):
	for row in board:
		for piece in row:
			if piece == " ":
				return False
	return True

#Problem 4
def connect_four():
	rows = 6
	columns = 7
	p_turn = 0

	board = make_c4_board(rows, columns)
	print_c4_board(board)

	while True:
		player = "R" if not p_turn else "Y"
		p_move = int(input(f"Player {player}, enter a column (1 - {columns}): ")) - 1
		if p_move not in range(0, columns):
			continue

		n_board = move_c4_piece(p_move, board, player)
		if n_board == "continue":
			print("Full Row!")
			continue
		else:
			board = n_board
		print_c4_board(board)

		if check_c4_win(board, rows, columns):
			print(f"{player} Wins!")
			break
		if full_c4_board(board):
			print("Cat Game!")
			break

		p_turn = 1 if not p_turn else 0
#End Problem 4

def get_adjacent_bombs(board):
	new_board = []
	for row in range(len(board)):
		new_row = []
		for col in range(len(board[0])):
			counter = 0
			if board[row][col] == " ":
				if row > 0:
					#TC
					if board[row - 1][col] == "B":
						counter += 1
					if col > 0:
						#TL
						if board[row - 1][col - 1] == "B":
							counter += 1
					if col < len(board[0]) - 1:
						#TR
						if board[row - 1][col + 1] == "B":
							counter += 1
				if col > 0:
					#CL
					if board[row][col - 1] == "B":
						counter += 1
				if col < len(board[0]) - 1:
					#CR
					if board[row][col + 1] == "B":
						counter += 1
				if row < len(board) - 1:
					#BC
					if board[row + 1][col] == "B":
						counter += 1
					if col > 0:
						#BL
						if board[row + 1][col - 1] == "B":
							counter += 1
					if col < len(board[0]) - 1:
						#BR
						if board[row + 1][col + 1] == "B":
							counter += 1
				new_row += [counter]
			else:
				new_row += ["B"]
		new_board += [new_row]
	return new_board

def make_ms_board(width, height, difficulty_pct, display_board=True):
	if not display_board:
		board = []
		num_bombs = int(width * height * difficulty_pct + 1)
		for bomb in range(num_bombs):
			board += ["B"]
		for not_bomb in range(width * height - num_bombs):
			board += [" "]

		random.shuffle(board)
		shuffle_board = []
		for row in range(height):
			new_row = []
			for col in range(width):
				new_row += [board[row * width + col]]
			shuffle_board += [new_row]

		return get_adjacent_bombs(shuffle_board)
	else:
		board = []
		for row in range(height):
			new_row = []
			for piece in range(width):
				new_row += ["#"]
			board.append(new_row)
		return board

def print_ms_board(board):
	for row in board:
		for piece in range(len(row)):
			print(f"{row[piece]}", end="")
		print("")

def check_ms_lose(display_board):
	for row in display_board:
		for piece in row:
			if piece == "B":
				return True
	return False

def check_ms_win(display_board, board):
	for row in range(len(display_board)):
		for piece in range(len(display_board)):
			if display_board[row][piece] == "#" and board[row][piece] != "B":
				return False
	return True

#Problem 5
def minesweeper(height, width, difficulty_pct):
	board = make_ms_board(width, height, difficulty_pct, display_board=False)
	display_board = make_ms_board(width, height, difficulty_pct)
	print_ms_board(display_board)

	while True:
		p_move = input(f"Enter a move, (row 1 - {height})(column 1 - {width}): ").strip()
		if len(p_move) != 2:
			continue
		p_move = (int(p_move[0]) - 1, int(p_move[1]) - 1)
		if not 0 <= p_move[0] <= width:
			continue
		if not 0 <= p_move[1] <= height:
			continue

		display_board[p_move[0]][p_move[1]] = board[p_move[0]][p_move[1]]
		print_ms_board(display_board)

		if check_ms_lose(display_board):
			print("You Lose :(")
			break
		if check_ms_win(display_board, board):
			print("You Win!")
			break
#End Problem 5

def print_sudoku_board(board):
	for row in range(len(board)):
		if row % 3 == 0:
			print("-" * (len(board[0]) * 3 - 2))
		for col in range(len(board[row])):
			if col % 3 == 0:
				print("|", end=" ")
			print(board[row][col], end=" ")
		print("|")
	print("-" * (len(board[0]) * 3 - 2))

def sudoku_valid_move(user_change, puzzle):
	if len(user_change) != 4:
		return False
	if int(user_change[0]) not in range(1, len(puzzle) + 1):
		return False
	if int(user_change[1]) not in range(1, len(puzzle[0]) + 1):
		return False
	if int(user_change[3]) not in range(1, 10):
		return False
	return True

def sudoku_solved(puzzle):
	sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	for row in puzzle:
		if sorted(row) != sorted_list:
			return False
	for col in range(len(puzzle[0])):
		curr_col = []
		for row in range(len(puzzle)):
			curr_col += [puzzle[row][col]]
		if sorted(curr_col) != sorted_list:
			return False
	for row in range(0, len(puzzle), 3):
		for col in range(0, len(puzzle[0]), 3):
			curr_3x3 = []
			for i in range(3):
				for j in range(3):
					curr_3x3 += [puzzle[row + i][col + j]]
			if sorted(curr_3x3) != sorted_list:
				return False
	return True

#Problem 6
def sudoku(puzzle):
	og_puzzle = []
	for row in puzzle:
		og_puzzle.append(row.copy())
	print_sudoku_board(puzzle)

	while True:
		user_change = input(f"Enter a move, (row 1 - {len(puzzle)})(column 1 - {len(puzzle[0])}) (number 1 - 9): ").strip()
		if not sudoku_valid_move(user_change, puzzle):
			continue
		user_change = (int(user_change[0]) - 1, int(user_change[1]) - 1, int(user_change[3]))
		if og_puzzle[user_change[0]][user_change[1]] != 0:
			continue
		puzzle[user_change[0]][user_change[1]] = user_change[2]
		print_sudoku_board(puzzle)

		if sudoku_solved(puzzle):
			print("You Win!")
			break
#End Problem 6

def print_hitori_board(board):
	for row in board:
		for piece in row:
			if piece == 0:
				print("#", end=" ")
			else:
				print(piece, end=" ")
		print("")

def hitori_valid_move(move, puzzle):
	if len(move) != 2:
		return False
	if not 0 < int(move[0]) < len(puzzle):
		return False
	if not 0 < int(move[1]) < len(puzzle[0]):
		return False
	return True

def hitori_connected(puzzle):
	return True

def hitori_solved(puzzle):
	for row in puzzle:
		#Checks 0s on touching horizontally
		for piece in range(len(row) - 1):
			if row[piece] == 0 and row[piece] == row[piece + 1]:
				return False
		#Checks no duplicates by row
		for i in range(len(row)):
			for j in range(len(row)):
				if i != j and row[i] == row[j] and row[i] != 0:
					return False

	for col in range(len(puzzle[0])):
		curr_col = []
		for row in range(len(puzzle)):
			curr_col += [puzzle[row][col]]

		#Checks 0s on touching vertically
		for piece in range(len(curr_col) - 1):
			if curr_col[piece] == 0 and curr_col[piece] == curr_col[piece + 1]:
				return False
		#Checks no duplicates by column
		for i in range(len(curr_col)):
			for j in range(len(curr_col)):
				if i != j and curr_col[i] == curr_col[j] and curr_col == 0:
					return False
	return hitori_connected(puzzle)

#Problem 7
def hitori(puzzle):
	og_puzzle = []
	for row in puzzle:
		og_puzzle.append(row.copy())
	print_hitori_board(puzzle)

	while True:
		move = input(f"Enter a move, (row 1 - {len(puzzle)})(col 1 - {len(puzzle[0])}): ").strip()
		if not hitori_valid_move(move, puzzle):
			continue
		move = (int(move[0]) - 1, int(move[1]) - 1)

		if puzzle[move[0]][move[1]] == 0:
			puzzle[move[0]][move[1]] = og_puzzle[move[0]][move[1]]
		else:
			puzzle[move[0]][move[1]] = 0

		print_hitori_board(puzzle)

		if hitori_solved(puzzle):
			print("You Win!")
			break









