import re
from collections import Counter

def parse_pgn_file(filename, move):
    with open(filename, 'r') as f:
        pgn_text = f.read()

    # Split the file into individual games
    games = re.findall(r'\[Event.*?\]\n\n(.*?)\n\n', pgn_text, re.DOTALL)

    # Split each game into a list of moves
    games = [re.findall(r'\d+\..*?\s(\w\w)', game) for game in games]

    # Get a list of pairs of moves in each game
    move_pairs = [(game[i], game[i+1]) for game in games for i in range(len(game) - 1)]

    # Filter the list of move pairs to include only those that start with the specified move
    move_pairs = [pair for pair in move_pairs if pair[0] == move]

    # Count the frequency of each move
    move_counts = Counter([pair[1] for pair in move_pairs])

    # Return the 5 most common moves
    return [move for move, count in move_counts.most_common(5)]

def get_most_popular_moves(filename, move):
    return parse_pgn_file(filename, move)

move = input('Enter a first move: ')
most_popular_moves = get_most_popular_moves('games.pgn', move)
print(f'The 5 most popular moves after {move} are: {most_popular_moves}')
