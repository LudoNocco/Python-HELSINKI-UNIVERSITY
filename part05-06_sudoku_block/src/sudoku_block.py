def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    numbers = []
    for row in range(row_no, row_no + 3):
        for column in range(column_no, column_no + 3):
            num = sudoku[row][column]
            if num > 0 and num in numbers:
                return False
            numbers.append(num)
    return True