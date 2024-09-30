try:
    with open('diary.txt', 'r') as file:
        entries = file.readlines()
except FileNotFoundError:
    entries = []

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    choice = input("Function: ")

    if choice == "1":
        entry = input("Diary entry: ")
        entries.append(entry + "\n")
        with open('diary.txt', 'a') as file:
            file.write(entry + "\n")
        print("Diary saved")

    elif choice == "2":
        print("Entries:")
        for entry in entries:
            print(entry.strip())

    elif choice == "0":
        print("Bye now!")
        break

    else:
        print("Invalid choice, please try again.")
