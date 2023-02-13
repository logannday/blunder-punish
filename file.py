import chess.pgn 
pgn = open("lichess_db_standard_rated_2013-01.pgn", encoding="utf-8")
first_game = chess.pgn.read_game(pgn)
print(first_game.headers["Event"])
board = first_game.board()
# for move in first_game.mainline_moves():
#     board.push(move)
print(first_game.game().next())  