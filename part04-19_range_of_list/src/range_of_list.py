def range_of_list(items: list) -> list:
    return max(items) - min(items)

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)