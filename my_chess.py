import chess
import chess.pgn
from collections import Counter

pgn = open("candidates.pgn")
games = []
while True:
    game= chess.pgn.read_game(pgn)
    if game is not None:
        games.append(game)
    else: 
        break

duda_rapport = games[0]
board = chess.Board()


i = 1
while True:
	if i % 2:
		current_move = input('what will your move be laddie?  ')
	else:
		current_move = input("What is your opponent's response?  ")	
	i += 1
	board_move = chess.Move.from_uci(current_move)
	board.push(board_move)
	print(board)
	#Removing games with a first move different from the 
	trimmed_games = []
	for game in games:

		if str(game.next().move) == current_move:
			trimmed_games.append(game.next())

	if len(trimmed_games) == 0:
		print("cum")
		break
	moves = []
	for game in trimmed_games:
		moves.append(str(game.next().move))


	# Count the number of occurrences of each move
	move_counts = Counter(moves)

	# Get the five most common moves
	top_five = move_counts.most_common(5)

	# Print the five most common moves
	for move, count in top_five:
		print(f"{move}: {count}")
	games = trimmed_games