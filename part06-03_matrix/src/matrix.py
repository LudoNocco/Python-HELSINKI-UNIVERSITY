# src/matrix.py

def read_matrix():
    with open("matrix.txt") as f:
        return [list(map(int, line.strip().split(','))) for line in f]

def matrix_sum():
    matrix = read_matrix()
    return sum(sum(row) for row in matrix)

def matrix_max():
    matrix = read_matrix()
    return max(max(row) for row in matrix)

def row_sums():
    matrix = read_matrix()
    return [sum(row) for row in matrix]

if __name__ == "__main__":
    print("Matrix sum:", matrix_sum())
    print("Maximum value in matrix:", matrix_max())
    print("Row sums:", row_sums())
