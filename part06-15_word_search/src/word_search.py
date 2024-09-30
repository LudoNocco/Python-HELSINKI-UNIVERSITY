def find_words(search_term: str):
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()

    matches = []
    if '*' in search_term:
        if search_term.startswith('*'):
            term = search_term[1:]
            matches = [word for word in words if word.endswith(term)]
        elif search_term.endswith('*'):
            term = search_term[:-1]
            matches = [word for word in words if word.startswith(term)]
    elif '.' in search_term:
        matches = [word for word in words if len(word) == len(search_term) and all(c1 == c2 or c2 == '.' for c1, c2 in zip(word, search_term))]
    else:
        matches = [word for word in words if word == search_term]

    return matches
