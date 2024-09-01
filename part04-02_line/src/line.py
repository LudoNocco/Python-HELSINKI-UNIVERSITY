def line(int, string):
    if string == "":
        print("*" * int)
    else:
        print(string[0] * int)

if __name__ == "__main__":
    line(5, "x")