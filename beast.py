import chess.pgn


# Open the PGN file
pgn = open("games.pgn")

# Create a dictionary to store the first moves
first_moves = {}

# Loop through all the games in the PGN file
while True:
    # Read the next game in the PGN file
    game = chess.pgn.read_game(pgn)
    # If there are no more games, break
    if game is None:
        break

    # Get the first move of the game
    first_move = game.board().san(game.variation(0))
    # If the first move is not in the dictionary, add it
    if first_move not in first_moves:
        first_moves[first_move] = 0
    # Increment the count for the first move
    first_moves[first_move] += 1

# Get the 5 most common first moves
top_five = sorted(first_moves, key=lambda x: first_moves[x], reverse=True)[:5]

# Print the top five first moves
print("Most common first moves:")
for i, move in enumerate(top_five):
    print(f"{i + 1}. {move} ({first_moves[move]})")

