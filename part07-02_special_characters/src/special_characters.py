import string

def separate_characters(my_string: str) -> tuple:

    ascii_letters = []
    punctuation_chars = []
    other_chars = []

    for char in my_string:
        if char in string.ascii_letters:
            ascii_letters.append(char)
        elif char in string.punctuation:
            punctuation_chars.append(char)
        else:
            other_chars.append(char)

    ascii_letters_str = ''.join(ascii_letters)
    punctuation_str = ''.join(punctuation_chars)
    other_chars_str = ''.join(other_chars)

    return (ascii_letters_str, punctuation_str, other_chars_str)
