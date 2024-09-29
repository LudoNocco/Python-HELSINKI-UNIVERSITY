def create_tuple(x: int, y: int, z: int):
    smallest = min(x, y, z)
    greatest = max(x, y, z)
    sum = x + y + z
    return smallest, greatest, sum