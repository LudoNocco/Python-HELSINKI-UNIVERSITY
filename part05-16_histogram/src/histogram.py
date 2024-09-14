def histogram(my_str: str):
    
    histogram = {}

    for char in my_str:
        if char in histogram:
            histogram[char] += 1
        else:
            histogram[char] = 1

    for key, value in histogram.items():
        print(f"{key} {value*'*'}")