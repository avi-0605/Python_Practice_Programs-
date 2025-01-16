def get_matrix_input(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        matrix.append(row)
    return matrix

def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Incompatible dimensions!")
        return None
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            value = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1[0])))
            row.append(value)
        result.append(row)
    return result

# Get user input
rows1, cols1 = map(int, input("Enter rows and cols for matrix 1: ").split())
matrix1 = []
for i in range(rows1):
    matrix1.append([int(x) for x in input(f"Enter row {i+1}: ").split()])

rows2, cols2 = map(int, input("Enter rows and cols for matrix 2: ").split())
matrix2 = []
for i in range(rows2):
    matrix2.append([int(x) for x in input(f"Enter row {i+1}: ").split()])

# Multiply matrices
result = multiply_matrices(matrix1, matrix2)

# Print result
if result:
    for row in result:
        print(row)
