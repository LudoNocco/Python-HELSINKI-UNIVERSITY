import string

def most_common_words(filename: str, lower_limit: int):
    with open(filename, 'r') as file:
        text = file.read()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()

    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    result = {word: count for word, count in word_count.items() if count >= lower_limit}
    return result
