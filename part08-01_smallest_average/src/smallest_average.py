def smallest_average(person1: dict, person2: dict, person3: dict):
    def average(person: dict):
        return (person["result1"] + person["result2"] + person["result3"]) / 3

    averages = [person1, person2, person3]
    
    smallest = min(averages, key=lambda person: average(person))
    
    return smallest
