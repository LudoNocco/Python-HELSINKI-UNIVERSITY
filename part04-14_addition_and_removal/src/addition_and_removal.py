list = []

while True:
    print(f"The list is now {list}")
    command = input("a(d)d, (r)emove or e(x)it:")

    if command == "d":
        item = len(list) + 1
        list.append(item)

    elif command == "r":
        list.pop(len(list) - 1)
        
    elif command == "x":
        break
    
print("Bye!")
