n = int(input("Layers: "))

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

size = 2 * n - 1
square = [[''] * size for _ in range(size)]

for i in range(n):
    char = alphabet[n - i - 1]
    for j in range(i, size - i):
        square[i][j] = char
        square[size - i - 1][j] = char
        square[j][i] = char
        square[j][size - i - 1] = char

for row in square:
    print(''.join(row))
