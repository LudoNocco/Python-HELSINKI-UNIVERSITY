class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents
        self._normalize()

    def _normalize(self):
        if self.__cents >= 100:
            self.__euros += self.__cents // 100
            self.__cents = self.__cents % 100

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __eq__(self, another):
        return self.__euros == another.__euros and self.__cents == another.__cents

    def __lt__(self, another):
        if self.__euros == another.__euros:
            return self.__cents < another.__cents
        return self.__euros < another.__euros

    def __gt__(self, another):
        if self.__euros == another.__euros:
            return self.__cents > another.__cents
        return self.__euros > another.__euros

    def __ne__(self, another):
        return not self == another

    def __add__(self, another):
        new_euros = self.__euros + another.__euros
        new_cents = self.__cents + another.__cents
        return Money(new_euros, new_cents)

    def __sub__(self, another):
        new_euros = self.__euros - another.__euros
        new_cents = self.__cents - another.__cents
        if new_cents < 0:
            new_euros -= 1
            new_cents += 100
        if new_euros < 0:
            raise ValueError("a negative result is not allowed")
        return Money(new_euros, new_cents)
