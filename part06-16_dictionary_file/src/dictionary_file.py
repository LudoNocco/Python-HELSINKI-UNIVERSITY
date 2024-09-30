try:
    with open('dictionary.txt', 'r') as file:
        dictionary = [line.strip().split(' - ') for line in file]
except FileNotFoundError:
    dictionary = []

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = input("Function: ")

    if function == "1":
        finnish_word = input("The word in Finnish: ")
        english_word = input("The word in English: ")
        dictionary.append((finnish_word, english_word))
        with open('dictionary.txt', 'a') as file:
            file.write(f"{finnish_word} - {english_word}\n")
        print("Dictionary entry added")

    elif function == "2":
        search_term = input("Search term: ")
        for finnish, english in dictionary:
            if search_term in finnish or search_term in english:
                print(f"{finnish} - {english}")

    elif function == "3":
        print("Bye!")
        break

    else:
        print("Invalid option, please try again.")
