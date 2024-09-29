import random

def words(n: int, beginning: str):
    with open('words.txt', 'r') as file:
        word_list = [line.strip() for line in file.readlines()]

    filtered_words = [word for word in word_list if word.startswith(beginning)]
    
    if len(filtered_words) < n:
        raise ValueError("Not enough words beginning with the specified string.")
    
    return random.sample(filtered_words, n)
