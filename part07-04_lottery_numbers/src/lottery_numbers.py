import random

def lottery_numbers(amount: int, lower: int, upper: int):
    numbers = random.sample(range(lower, upper + 1), amount)
    return sorted(numbers)