class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is empty(self) -> bool:
        return len(self.persons) == 0

    def print_contents(self):
        combined_height = 0
        for person in self.persons:
            combined_height += person.height
        print(f"There are {len(self.persons)} persons in the room. Their combined height is {combined_height} cm.")
        for person in self.persons: 
            print(person)

    def shortest(self) -> Person:
        return min(self.persons, key = lambda x : x.height)

    def remove_shortest(self) -> Person:
        return self.persons.pop(self.persons.index(self.shortest()))
    
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name
