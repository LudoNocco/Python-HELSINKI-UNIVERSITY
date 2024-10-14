import re

def is_dotw(my_string: str):
    return bool(re.match(r"^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)$", my_string))

def all_vowels(my_string: str):
    return bool(re.fullmatch(r"[aeiou]+", my_string))

def time_of_day(my_string: str):
    return bool(re.fullmatch(r"(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])", my_string))