num_items = int(input("How many items: "))

items_list = []

for i in range(num_items):
    item = int(input(f"Item {i + 1}: "))
    items_list.append(item)

print(items_list)