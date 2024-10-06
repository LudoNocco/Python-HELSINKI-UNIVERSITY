class RealProperty:
    def __init__(self, rooms: int, square_metres: int, price_per_sqm: int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    def bigger(self, compared_to):
        return self.square_metres > compared_to.square_metres

    def price_difference(self, compared_to):
        self_total_price = self.square_metres * self.price_per_sqm
        compared_total_price = compared_to.square_metres * compared_to.price_per_sqm
        return abs(self_total_price - compared_total_price)

    def more_expensive(self, compared_to):
        self_total_price = self.square_metres * self.price_per_sqm
        compared_total_price = compared_to.square_metres * compared_to.price_per_sqm
        return self_total_price > compared_total_price
