class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.sum_of_numbers = 0

    def add_number(self, number: int):
        self.numbers += 1
        self.sum_of_numbers += number

    def count_numbers(self):
        return self.numbers

    def get_sum(self):
        return self.sum_of_numbers

    def average(self):
        if self.numbers == 0:
            return 0
        return self.sum_of_numbers / self.numbers

all_stats = NumberStats()
even_stats = NumberStats()
odd_stats = NumberStats()

print("Please type in integer numbers: ")
while True:
    number = int(input())
    if number == -1:
        break
    
    all_stats.add_number(number)
    
    if number % 2 == 0:
        even_stats.add_number(number)
    else:
        odd_stats.add_number(number)

print("Sum of numbers:", all_stats.get_sum())
print("Mean of numbers:", all_stats.average())
print("Sum of even numbers:", even_stats.get_sum())
print("Sum of odd numbers:", odd_stats.get_sum())
