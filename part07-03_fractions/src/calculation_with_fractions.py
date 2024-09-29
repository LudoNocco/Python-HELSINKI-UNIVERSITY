from fractions import Fraction

def fractionate(amount: int):
    fraction = Fraction(1, amount)
    return [fraction] * amount