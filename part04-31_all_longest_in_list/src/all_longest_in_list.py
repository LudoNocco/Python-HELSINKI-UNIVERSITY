def all_the_longest(list):
    max_length = max(len(s) for s in list)
    return [s for s in list if len(s) == max_length]