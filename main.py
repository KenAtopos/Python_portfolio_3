def draw_board(board):
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[0], board[1], board[2]))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[3], board[4], board[5]))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[6], board[7], board[8]))
    print("     |     |")


def get_player_move(board, player):
    valid_move = False
    while not valid_move:
        move = input("Player " + player + ", enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == ' ':
            valid_move = True
        else:
            print("Invalid move. Please try again.")
    return int(move)


def check_win(board):
    winning_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # vertical
        [0, 4, 8], [2, 4, 6] # diagonal
    ]
    for positions in winning_positions:
        if board[positions[0]] == board[positions[1]] == board[positions[2]] and board[positions[0]] != ' ':
            return board[positions[0]]
    return None


def main():
    board = [' '] * 9
    player = 'X'
    winner = None
    while winner is None:
        draw_board(board)
        move = get_player_move(board, player)
        board[move-1] = player
        winner = check_win(board)
        if winner is None:
            if ' ' not in board:
                print("Tie game.")
                return
            player = 'O' if player == 'X' else 'X'
    draw_board(board)
    print("Congratulations, player " + winner + " won!")


if __name__ == "__main__":
    main()
