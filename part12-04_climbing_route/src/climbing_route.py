class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

def sort_by_length(routes: list):
    return sorted(routes, key=lambda x: x.length, reverse=True)

def sort_by_difficulty(routes: list):
    return sorted(routes, key=lambda x: (x.grade, x.length), reverse=True)