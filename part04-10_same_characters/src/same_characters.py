def same_chars(text, int1, int2):
    try:
        return text[int1] == text[int2]
    except IndexError:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))