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



first_move = input('what will your first move be laddie?')

#Removing games with a first move different from the 
trimmed_games = []
for game in games:
	if str(game.next().move) == first_move:
		trimmed_games.append(game)


moves = []
for game in trimmed_games:
	moves.append(str(game.next().next().move))


# Count the number of occurrences of each move
move_counts = Counter(moves)

# Get the five most common moves
top_five = move_counts.most_common(5)

# Print the five most common moves
for move, count in top_five:
    print(f"{move}: {count}")
games = trimmed_games