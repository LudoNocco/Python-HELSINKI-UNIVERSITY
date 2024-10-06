class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []

    def add_item(self, item: Item):
        if self.weight() + item.weight() <= self.__max_weight:
            self.__items.append(item)

    def weight(self):
        return sum(item.weight() for item in self.__items)

    def print_items(self):
        for item in self.__items:
            print(item)

    def heaviest_item(self):
        if not self.__items:
            return None
        return max(self.__items, key=lambda item: item.weight())

    def __str__(self):
        num_items = len(self.__items)
        item_str = "item" if num_items == 1 else "items"
        return f"{num_items} {item_str} ({self.weight()} kg)"

class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcases = []

    def add_suitcase(self, suitcase: Suitcase):
        if self.weight() + suitcase.weight() <= self.__max_weight:
            self.__suitcases.append(suitcase)

    def weight(self):
        return sum(suitcase.weight() for suitcase in self.__suitcases)

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

    def __str__(self):
        num_suitcases = len(self.__suitcases)
        suitcase_str = "suitcase" if num_suitcases == 1 else "suitcases"
        remaining_weight = self.__max_weight - self.weight()
        return f"{num_suitcases} {suitcase_str}, space for {remaining_weight} kg"

