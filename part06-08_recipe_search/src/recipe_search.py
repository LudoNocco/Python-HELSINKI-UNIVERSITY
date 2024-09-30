def search_by_name(filename: str, word: str):
    with open(filename, 'r') as file:
        content = file.read()

    recipes = []
    search_term = word.lower()
    entries = content.strip().split('\n\n')  # Split recipes by double newlines

    for entry in entries:
        lines = entry.strip().split('\n')
        recipe_name = lines[0].strip()
        if search_term in recipe_name.lower():
            recipes.append(recipe_name)
    return recipes

def search_by_time(filename: str, time: int):
    with open(filename, 'r') as file:
        content = file.read()

    recipes = []
    entries = content.strip().split('\n\n')

    for entry in entries:
        lines = entry.strip().split('\n')
        recipe_name = lines[0].strip()
        prep_time = int(lines[1].strip())
        if prep_time <= time:
            recipes.append(f"{recipe_name}, preparation time {prep_time} min")
    return recipes


def search_by_ingredient(filename: str, ingredient: str):
    with open(filename, 'r') as file:
        content = file.read()

    recipes = []
    search_ingredient = ingredient.lower()
    entries = content.strip().split('\n\n')

    for entry in entries:
        lines = entry.strip().split('\n')
        recipe_name = lines[0].strip()
        prep_time = int(lines[1].strip())
        ingredients = [line.strip().lower() for line in lines[2:]]
        if search_ingredient in ingredients:
            recipes.append(f"{recipe_name}, preparation time {prep_time} min")
    return recipes
