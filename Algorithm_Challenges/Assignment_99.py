def get_matrix_input(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1} (space-separated): ").split()))
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result

# Example usage:
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("Enter elements for the first matrix:")
matrix1 = get_matrix_input(rows, cols)

print("Enter elements for the second matrix:")
matrix2 = get_matrix_input(rows, cols)

# Perform matrix addition
sum_matrix = add_matrices(matrix1, matrix2)

# Print the result
print("Sum of the matrices:")
for row in sum_matrix:
    print(row)
