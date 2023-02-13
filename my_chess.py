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
board = duda_rapport.board()


first_moves = []
for game in games:
	first_moves.append(str(game.next().move))
	print(game.next().move)
print(first_moves)

# Count the number of occurrences of each move
move_counts = Counter(first_moves)

# Get the five most common moves
top_five = move_counts.most_common(5)

# Print the five most common moves
for move, count in top_five:
    print(f"{move}: {count}")

first_move = input('what will your first move be laddie?')

trimmed_games = []
for game in games:
	if str(game.next().move) == first_move:
		trimmed_games.append(game)
for game in trimmed_games:
	print(game.next().move)

