#Check if a Matrix is Symmetric Determine if a given square matrix is symmetric (equal to its transpose).
def get_matrix_input(n):
    matrix = []
    for i in range(n):
        row = [int(x) for x in input(f"Enter row {i+1}: ").split()]
        matrix.append(row)
    return matrix

def is_symmetric(matrix):
    n = len(matrix)
    # Check if the matrix is equal to its transpose
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

# Get user input for matrix size (n x n)
n = int(input("Enter the size of the square matrix (n): "))

# Get matrix elements from the user
matrix = get_matrix_input(n)

# Check if the matrix is symmetric
if is_symmetric(matrix):
    print("The matrix is symmetric.")
else:
    print("The matrix is not symmetric.")
