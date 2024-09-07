def longest_series_of_neighbours(list):
    max_length = 0
    current_length = 1

    for i in range(1, len(list)):
        if abs(list[i] - list[i-1]) == 1:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1
    return max(max_length, current_length)