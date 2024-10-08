def remove_smaller_than(numbers: list, limit: int) -> list:
    return list(filter(lambda x: x >= limit, numbers))