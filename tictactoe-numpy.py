import numpy as np

# Create the game board
board = np.zeros((3, 3), dtype=int)


# Define a function to print the game board
def print_board():
    for row in board:
        print(
            " | ".join(
                ["X" if cell == 1 else "O" if cell == 2 else " " for cell in row]
            )
        )
        print("-" * 9)


# Define a function to check if there is a winner
def check_winner():
    rows_sum = np.sum(board, axis=1)
    cols_sum = np.sum(board, axis=0)
    diagonal_sum1 = np.trace(board)
    diagonal_sum2 = np.trace(np.fliplr(board))

    sums = np.concatenate((rows_sum, cols_sum, [diagonal_sum1, diagonal_sum2]))

    if any(abs(s) == 3 for s in sums):
        return True
    return False


# Define a function to make a move
def make_move(row, col, player):
    if row < 0 or row >= 3 or col < 0 or col >= 3 or board[row][col] != 0:
        print("Invalid move! Try again.")
        return False

    board[row][col] = player
    return True


# Start the game
current_player = 1

while True:
    print_board()
    print(f"Player {current_player}'s turn")

    row = int(input("Enter the row (0-2): "))
    col = int(input("Enter the column (0-2): "))

    if make_move(row, col, current_player):
        if check_winner():
            print_board()
            print(f"Player {current_player} wins!")
            break

        if 0 not in board:
            print_board()
            print("It's a tie!")
            break

        current_player = 2 if current_player == 1 else 1
