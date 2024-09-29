# Read the word list from the file and store it in a set for quick lookup
with open("wordlist.txt") as f:
    word_list = set(line.strip().lower() for line in f)

# Ask for user input
user_input = input("Write text: ")

# Process the input text
words = user_input.split()

# Check each word and add stars around misspelled words
corrected_text = []
for word in words:
    # Strip punctuation and lowercase the word to make the check case-insensitive
    clean_word = ''.join(char for char in word if char.isalpha()).lower()
    if clean_word not in word_list:
        corrected_text.append(f"*{word}*")
    else:
        corrected_text.append(word)

# Join the corrected words and print the result
print(' '.join(corrected_text))
