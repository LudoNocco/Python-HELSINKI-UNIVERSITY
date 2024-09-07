def mean(items: list) -> float:
    return sum(items) / len(items)

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)