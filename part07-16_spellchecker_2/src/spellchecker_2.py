import difflib

with open('wordlist.txt', 'r') as file:
    wordlist = [line.strip() for line in file]

text = input("write text: ")
words = text.split()
corrected_text = []
misspelled_words = {}

for word in words:
    clean_word = ''.join(char for char in word if char.isalpha()).lower()
    if clean_word in wordlist:
        corrected_text.append(word)
    else:
        corrected_text.append(f"*{word}*")
        suggestions = difflib.get_close_matches(clean_word, wordlist)
        if suggestions:
            misspelled_words[clean_word] = suggestions

print(' '.join(corrected_text))

if misspelled_words:
    print("suggestions:")
    for word, suggestions in misspelled_words.items():
        print(f"{word}: {', '.join(suggestions)}")
