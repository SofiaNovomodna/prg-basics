def transpose_matrix(m):
    rows = len(m)
    cols = len(m[0])

    # Create empty transposed matrix
    t = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(m[r][c])
        t.append(new_row)

    return t


def print_matrix(m):
    for row in m:
        for value in row:
            print(value, end=" ")
        print()


# Given matrices
m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

m2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

# Transpose and print
print("Matrix 1 transposed:")
print_matrix(transpose_matrix(m1))

print("\nMatrix 2 transposed:")
print_matrix(transpose_matrix(m2))