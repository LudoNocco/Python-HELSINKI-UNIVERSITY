values_list = []

while True:
    item = int(input("New item: "))

    if item == 0:
        print("Bye!")
        break
    
    values_list.append(item)
    print(f"The list now: {values_list}")
    print(f"The list in order: {sorted(values_list)}")
