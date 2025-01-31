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
	for row in board:
		for piece in range(len(row) - 3):
			if (row[piece] != " " and
				row[piece + 0] == 
				row[piece + 1] ==
				row[piece + 2] ==
				row[piece + 3]):
				return True

	for col in range(len(board[0])):
		for row in range(len(board) - 3):
			if (board[row][col] != " " and 
				board[row + 0][col] == 
				board[row + 1][col] ==
				board[row + 2][col] ==
				board[row + 3][col]):
				return True

	for row in range(len(board) - 3):
		for col in range(len(board[0]) - 3):
			if (board[col][row] != " " and
				board[col + 0][row + 0] ==
				board[col + 1][row + 1] ==
				board[col + 2][row + 2] ==
				board[col + 3][row + 3]):
				return True

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

#Problem 5
def minesweeper(width, height, difficulty_pct):
	print("You win!")

#Problem 6
def sudoku(puzzle):
	print("This game's boring \"ash\" ")

#Problem 7
def hitori(puzzle):
	print("Je sais pas ce qui passe")
