def tic_tac_toe():
    board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

    def print_board():
        for row in board:
            print(" ".join(row))

    while True:
        print_board()

        player_choice = input("Player 1, choose a square (1-9): ")
        board[player_choice // 3 - 1][player_choice % 3 - 1] = "X"

        if check_winner(board):
            print("Player 1 wins!")
            break

        print_board()

        player_choice = input("Player 2, choose a square (1-9): ")
        board[player_choice // 3 - 1][player_choice % 3 - 1] = "O"

        if check_winner(board):
            print("Player 2 wins!")
            break

    print("Game over!")


def check_winner(board):
    for row in board:
        if all(row[i] == row[0] for i in range(len(row))):
            return True

    for column in range(len(board[0])):
        if all(board[i][column] == board[0][column] for i in range(len(board))):
            return True

    if all(board[i][i] == board[0][0] for i in range(len(board))):
        return True

    if all(
        board[i][len(board) - 1 - i] == board[0][len(board) - 1]
        for i in range(len(board))
    ):
        return True

    return False


tic_tac_toe()
