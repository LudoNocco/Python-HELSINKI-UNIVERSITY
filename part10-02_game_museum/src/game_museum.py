class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int):
        self.name = name
        self.publisher = publisher
        self.year = year

class GameWarehouse:
    def __init__(self):
        self._games = []

    def add_game(self, game: ComputerGame):
        self._games.append(game)

    def list_games(self):
        return self._games

class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()

    def list_games(self):
        return [game for game in self._games if game.year < 1990]
