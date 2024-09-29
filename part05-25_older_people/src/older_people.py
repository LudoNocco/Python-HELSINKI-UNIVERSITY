def older_people(people: list, year: int):
    return [person[0] for person in people if person[1] < year]