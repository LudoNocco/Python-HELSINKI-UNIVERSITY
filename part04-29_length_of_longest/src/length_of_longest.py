def length_of_longest(my_list: list) -> int:
    return len(max(my_list, key=len))