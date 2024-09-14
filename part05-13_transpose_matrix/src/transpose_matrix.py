def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            # Swap the elements at (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]