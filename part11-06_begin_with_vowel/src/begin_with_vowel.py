def begin_with_vowel(words: list) -> list:
    return list(filter(lambda x: x[0] in "aeiouAEIOU", words))