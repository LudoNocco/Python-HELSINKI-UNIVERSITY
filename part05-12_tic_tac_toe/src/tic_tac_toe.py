def play_turn(game_board, x, y, piece):
    if not (0 <= x < 3 and 0 <= y < 3):
        return False
    
    if game_board[y][x] == "":
        game_board[y][x] = piece
        return True
    else:
        return False
