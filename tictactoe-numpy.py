import numpy as np


# Create the game board
def create_board():
    return np.zeros((3, 3), dtype=int)


# Define a function to print the game board
def print_board(board):
    for row in board:
        print(
            " | ".join(
                ["X" if cell == 1 else "O" if cell == 2 else " " for cell in row]
            )
        )
        print("-" * 9)


# Define a function to check if there is a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    return (
        np.any(np.all(board == player, axis=1))
        or np.any(np.all(board == player, axis=0))  # rows
        or np.all(np.diag(board) == player)  # columns
        or np.all(np.diag(np.fliplr(board)) == player)  # main diagonal
    )  # anti-diagonal


def is_board_full(board):
    return not any(0 in row for row in board)


# Define a function to make a move
def make_move(board, player):
    while True:
        print(f"Player {player}'s turn")
        try:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == 0:
                board[row][col] = player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_game():
    board = create_board()
    player = 1

    while True:
        print_board(board)
        make_move(board, player)

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        player = 3 - player  # Switch player (1 -> 2 or 2 -> 1)


if __name__ == "__main__":
    play_game()
