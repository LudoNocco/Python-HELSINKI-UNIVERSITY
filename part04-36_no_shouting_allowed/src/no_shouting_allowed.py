def no_shouting(my_list: list) -> list:
    return [word for word in my_list if not word.isupper()]