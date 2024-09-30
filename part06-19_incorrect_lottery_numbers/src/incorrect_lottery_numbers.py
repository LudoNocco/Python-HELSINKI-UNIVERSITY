def filter_incorrect():
    def is_valid_lottery_line(line: str) -> bool:
        try:
            week, numbers = line.split(';')
            if not week.startswith("week ") or not week[5:].isdigit():
                return False
            numbers = numbers.split(',')
            if len(numbers) != 7:
                return False
            num_set = set()
            for num in numbers:
                if not num.isdigit():
                    return False
                number = int(num)
                if number < 1 or number > 39 or number in num_set:
                    return False
                num_set.add(number)
            return True
        except:
            return False

    with open('lottery_numbers.csv', 'r') as infile, open('correct_numbers.csv', 'w') as outfile:
        for line in infile:
            line = line.strip()
            if is_valid_lottery_line(line):
                outfile.write(line + "\n")
