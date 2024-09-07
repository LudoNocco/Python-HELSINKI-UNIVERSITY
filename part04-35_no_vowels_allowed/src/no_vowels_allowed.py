def no_vowels(my_string: str) -> str:
    return "".join([x for x in my_string if x not in "aeiou"])