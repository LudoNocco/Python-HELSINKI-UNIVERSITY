def dict_of_numbers():
    ones = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }
    teens = {
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
    }
    tens = {
        20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
        60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
    }

    numbers = {0: 'zero'}
    numbers.update(ones)
    numbers.update(teens)
    numbers.update(tens)

    for i in range(20, 100):
        if i not in numbers:
            numbers[i] = tens[i - (i % 10)] + '-' + ones[i % 10]

    return numbers