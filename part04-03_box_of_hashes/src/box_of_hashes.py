# Copy here code of line function from previous exercise
def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)

def box_of_hashes(height):
    i = 1
    while i <= height:
        line(10, "#")
        i += 1

if __name__ == "__main__":
    box_of_hashes(5)
