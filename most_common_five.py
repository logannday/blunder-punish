import chess
import chess.pgn

# Read the PGN file
with open("candidates.pgn") as pgn_file:
    # Create a database of all the first moves in the games
    first_moves = []
    for game in chess.pgn.read_game(pgn_file):
        board = game.board()
        moves = game.mainline_moves()
        first_moves.append(game.next().move)

# Count the number of occurrences of each move
from collections import Counter
move_counts = Counter(first_moves)

# Get the five most common moves
top_five = move_counts.most_common(5)

# Print the five most common moves
for move, count in top_five:
    print(f"{move}: {count}")
