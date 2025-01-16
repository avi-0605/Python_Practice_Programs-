#Tic-Tac-Toe Implement the 2-player Tic-Tac-Toe game on the console.
# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if there is a winner
def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True
    
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    
    return False

# Function to check if the board is full (no more moves)
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Function for the main game loop
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]  # Initialize a 3x3 board
    current_player = "X"  # Player X starts first
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn:")
        
        # Get valid input from the player
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter column (1-3): ")) - 1
        
        if row not in range(3) or col not in range(3) or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        
        # Make the move
        board[row][col] = current_player
        
        # Check if the current player has won
        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check if the board is full (a draw)
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
tic_tac_toe()
