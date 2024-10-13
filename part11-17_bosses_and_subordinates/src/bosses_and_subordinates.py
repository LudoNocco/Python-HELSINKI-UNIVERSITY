def count_subordinates(employee: 'Employee'):
    if len(employee.subordinates) == 0:
        return 0
    else:
        return sum([count_subordinates(x) + 1 for x in employee.subordinates])

class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)
