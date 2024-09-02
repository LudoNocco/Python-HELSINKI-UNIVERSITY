def first_word(sentence):
    # Split the sentence into words and return the first word
    return sentence.split()[0]

def second_word(sentence):
    # Split the sentence into words and return the second word
    return sentence.split()[1]

def last_word(sentence):
    # Split the sentence into words and return the last word
    return sentence.split()[-1]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))