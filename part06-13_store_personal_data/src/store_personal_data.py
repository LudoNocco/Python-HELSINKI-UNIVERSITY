def store_personal_data(person: tuple):
    with open('people.csv', 'a') as file:
        file.write(f"{person[0]};{person[1]};{person[2]}\n")
