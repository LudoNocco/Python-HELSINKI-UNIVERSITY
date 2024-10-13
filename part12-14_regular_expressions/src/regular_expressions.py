import re

def is_dotw(my_string: str) -> bool:
    return re.match(r"(Mon|Tue|Wed|Thu|Fri|Sat|Sun)", my_string)

def all_vowels(my_string: str) -> bool:
    return len([x for x in my_string if x not in "aeiou"]) == 0

def time_of_day(my_string: str) -> bool:
    return re.match(r"([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]", my_string)