#Backtracking: N-Queens Implement the N-Queens puzzle using backtracking.
def is_safe(board, row, col, N):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(board, row, N, solutions):
    # If all queens are placed, add the current solution to the list
    if row == N:
        solutions.append(board[:])  # Make a copy of the board
        return
    
    # Try placing the queen in every column of the current row
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col  # Place queen in the current column
            solve_n_queens(board, row + 1, N, solutions)  # Recurse for next row
            board[row] = -1  # Backtrack by removing the queen

def n_queens(N):
    solutions = []  # List to store all the solutions
    board = [-1] * N  # Initialize the board with -1 (no queens placed)
    
    solve_n_queens(board, 0, N, solutions)
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print('.' * row + 'Q' + '.' * (len(solution) - row - 1))  # Print the board
        print()

# Example usage
N = 4  # Change N to test for different sizes
solutions = n_queens(N)
print(f"Total solutions for {N}-Queens: {len(solutions)}")
print_solutions(solutions)
