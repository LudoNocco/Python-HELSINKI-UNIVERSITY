class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers

    def __str__(self):
        return f'{self.name}, superpowers: {self.superpowers}'
    
class SuperGroup:
    def __init__(self, name: str, location: str, members: list = []):
        self.__name = name
        self.__location = location
        self.__members = members

    @property
    def add_member(hero: SuperHero):
        self.__members.append(hero)

    @property
    def print_group(self):
        print(self.__members)  
