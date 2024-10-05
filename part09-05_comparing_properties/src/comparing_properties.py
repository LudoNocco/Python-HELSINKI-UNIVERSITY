def bigger(self, compared_to):
    if self.price_per_sqm > compared_to.price_per_sqm:
        return True
    else:
        return False

def price_difference(self, compared_to):
    if self.price_per_sqm > compared_to.price_per_sqm:
        return self.price_per_sqm - compared_to.price_per_sqm
    else:
        return compared_to.price_per_sqm - self.price_per_sqm
    
def more_expensive(self, compared_to):
    if self.price_per_sqm > compared_to.price_per_sqm:
        return True
    else:
        return False

class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        bigger = 0
        price_difference = 0
        more_expensive = 0
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm
