#note, this file prints the most common first five moves without using python chess
import re
from collections import Counter

def parse_pgn_file(filename):
    with open(filename, 'r') as f:
        pgn_text = f.read()

    # Split the file into individual games
    games = re.findall(r'\[Event.*?\]\n\n(.*?)\n\n', pgn_text, re.DOTALL)

    # Split each game into a list of moves
    games = [re.findall(r'\d+\..*?\s(\w\w)', game) for game in games]
    print(games[0])


    # Get a list of the first move in each game
    first_moves = [game[0] for game in games if game]

    # Count the frequency of each move
    move_counts = Counter(first_moves)

    # Return the most common move
    return move_counts.most_common(1)[0][0]



first_move = parse_pgn_file('games.pgn')
print(f'The most common first move is {first_move}')