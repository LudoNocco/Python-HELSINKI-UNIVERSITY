class LotteryNumbers:
    def __init__(self, week: int, numbers: list):
        self.week = week
        self.numbers = numbers

    def number_of_hits(self, numbers: list):
        return sum(1 for number in numbers if number in self.numbers)

    def hits_in_place(self, numbers: list):
        return [n if n in self.numbers else -1 for n in numbers]
