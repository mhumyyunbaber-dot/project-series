def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    print("🎮 Welcome to Tic‑Tac‑Toe!")
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn.")

        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))
        except ValueError:
            print("❌ Invalid input. Enter numbers only.")
            continue

        if row not in [0,1,2] or col not in [0,1,2]:
            print("❌ Invalid position. Try again.")
            continue

        if board[row][col] != " ":
            print("⚠️ Position already taken. Try again.")
            continue

        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print(f"🎉 Player {player} wins!")
            break

        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("🤝 It's a tie!")
            break

        turn += 1

tic_tac_toe()
