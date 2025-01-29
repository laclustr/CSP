#Tic Tac Toe

def make_board(rows=3, columns=3):
    board = []
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(" ")
        board.append(temp)
    return board
def print_board(board):
	
	for row in board:
		output = ""
		for val in row:
			output += val + "|"
		print(output[:-1])
		if id(row) != id(board[-1]):
			print("-" * 5)
def check_win(board):
	for row in board:
		piece = row[0]
		if piece != " " and piece == row[1] and piece == row[2]:
			return row[0]
	
	for col in range(len(board[0])):
		if (
			board[0][col] != " " and 
	  		board[0][col] == board[1][col] and 
			board[0][col] == board[2][col]
			):
			return board[0][col]
	
	if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
		return board[0][0]
	if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
		return board[0][2]
	
	for col in range(len(board[0])):
		empty_row = False
		for row in range(len(board)):
			if board[row][col] == " ":
				empty_row = True
			if empty_row:
				return ""
	return "cat"


player = "X"
board = make_board()
game_over = False
print_board(board)

while not game_over:
	player_move = input("Enter Move (row)(column): ")
	r = int(player_move[0])
	c = int(player_move[1])
	if board[r][c] == " ":
		board[r][c] = player
		print_board(board)
		winner = check_win(board)

		if winner == player:
			print(f"{player} wins!")
			break
		elif winner == "cat":
			print("It's a draw!")
			break
		if player == "X":
			player = "O"
		else:
			player = "X"
	else:
		continue
	
