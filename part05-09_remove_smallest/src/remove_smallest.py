def remove_smallest (numbers: list) -> list:
    if len(numbers) != 0:
        numbers.remove(min(numbers))
