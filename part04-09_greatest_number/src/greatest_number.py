def greatest_number(num1, num2, num3):
    if num1 < num2:
        if num2 < num3:
            greatest = num3
        else:
            greatest = num2
    else:
        greatest = num1
    return greatest

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(4, 5, 8)
    print(greatest)