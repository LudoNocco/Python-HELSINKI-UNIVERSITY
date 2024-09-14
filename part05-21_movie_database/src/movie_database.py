def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    my_dict = {"name": name, "director": director, "year": year, "runtime": runtime}
    database.append(my_dict)