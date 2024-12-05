def tic_tac_toe():
    board = [["-" for _ in range(3)] for _ in range(3)]

    def print_board():
        for i in range(5):
            if i % 2 == 0:
                print(" | ".join(board[i // 2]))
            else:
                print("-" * 9)

    def make_move(player, choice):
        row, col = divmod(choice - 1, 3)
        if board[row][col] == "-":
            board[row][col] = player
            return True
        else:
            print("Invalid move! Try again.")
            return False

    def check_winner():
        for i in range(3):
            # Check rows and columns
            if all(board[i][j] == board[i][0] and board[i][0] != "-" for j in range(3)):
                return True
            if all(board[j][i] == board[0][i] and board[0][i] != "-" for j in range(3)):
                return True

        # Check diagonals
        if all(board[i][i] == board[0][0] and board[0][0] != "-" for i in range(3)):
            return True
        if all(board[i][2 - i] == board[0][2] and board[0][2] != "-" for i in range(3)):
            return True

        return False

    current_player = "X"

    while True:
        print_board()

        player_choice = int(input(f"\nPlayer {current_player}, choose a square (1-9): "))
        if 1 <= player_choice <= 9:
            if make_move(current_player, player_choice):
                if check_winner():
                    print_board()
                    print(f"Player {current_player} wins!")
                    break
                elif all(cell != "-" for row in board for cell in row):
                    print_board()
                    print("It's a tie!")
                    break

                current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid input! Please choose a number between 1 and 9.")

    print("Game over!")


tic_tac_toe()
