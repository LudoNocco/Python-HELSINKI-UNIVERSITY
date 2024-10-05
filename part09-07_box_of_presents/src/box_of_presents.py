class Present:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"Present({self.name}, {self.weight})"
    
class Box:
    def __init__(self):
        self.presents = []

    def add_present(self, present):
        self.presents.append(present)

    def total_weight(self):
        return sum([present.weight for present in self.presents])