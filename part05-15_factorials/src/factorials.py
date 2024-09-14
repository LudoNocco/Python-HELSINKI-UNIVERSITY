def factorials(n: int) -> dict:
    my_dict = {}
    for i in range(1, n + 1):
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        my_dict[i] = factorial
    return my_dict