# Copy here code of line function from previous exercise
def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)

def triangle(size):
    i = 1
    while i <= size:
        line(size, "#")
        i + 1

if __name__ == "__main__":
    triangle(5)
