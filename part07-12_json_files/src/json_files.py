import json

def print_persons(filename: str):
    with open(filename) as f:
        data = json.load(f)
        for person in data:
            print(f"{person['name']} {person['age']} years ({', '.join(person['hobbies'])})")