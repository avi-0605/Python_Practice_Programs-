def get_matrix_input(rows, cols):
    matrix = []
    for i in range(rows):
        row = [int(x) for x in input(f"Enter row {i+1}: ").split()]
        matrix.append(row)
    return matrix

def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Get user input for matrix dimensions
rows, cols = map(int, input("Enter rows and cols for the matrix: ").split())

# Get matrix elements from the user
matrix = get_matrix_input(rows, cols)

# Compute transpose
transposed_matrix = transpose_matrix(matrix)

# Print the transposed matrix
print("Transposed Matrix:")
for row in transposed_matrix:
    print(row)
