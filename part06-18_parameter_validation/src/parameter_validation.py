def new_person(name: str, age: int) -> tuple:
    if not name or len(name.split()) < 2 or len(name) > 40:
        raise ValueError("Invalid name")
    if not (0 <= age <= 150):
        raise ValueError("Invalid age")
    
    return (name, age)
