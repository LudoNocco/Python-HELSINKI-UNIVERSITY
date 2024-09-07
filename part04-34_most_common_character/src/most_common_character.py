def most_common_character(my_string):
    return max(set(my_string), key=my_string.count)