my_list = [1, 2, 3, 4, 5]

while True:
    Index = int(input("Index: "))
    if Index == -1:
        break
    if 0 <= Index < len(my_list):
        New_value = int(input("New value: "))
        my_list[Index] = New_value
        print(my_list)