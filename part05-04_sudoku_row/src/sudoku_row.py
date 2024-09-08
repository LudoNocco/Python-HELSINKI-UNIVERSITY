def row_correct(sudoku: list, row_no: int) -> bool:

    row = sudoku[row_no]
    seen = set()
    for num in row:
        if num == 0:
            continue
        if num < 1 or num > 9:
            return False
        if num in seen:
            return False
        seen.add(num)
    return True