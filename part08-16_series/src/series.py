class Series:
    def __init__(self, title, seasons, genres):
        self.title = title  
        self.seasons = seasons
        self.genres = genres
        self.ratings = []

    def rate(self, rating: int):
        self.ratings.append(rating)

    def __str__(self):
        if len(self.ratings) == 0:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {', '.join(self.genres)}\nno ratings"
        else:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {', '.join(self.genres)}\n{len(self.ratings)} ratings, average {sum(self.ratings) / len(self.ratings):.1f} points"

def minimum_grade(grade: float, series_list: list):
    result = []
    for series in series_list:
        if len(series.ratings) > 0 and (sum(series.ratings) / len(series.ratings)) >= grade:
            result.append(series)
    return result

def includes_genre(genre: str, series_list: list):
    result = []
    for series in series_list:
        if genre in series.genres:
            result.append(series)
    return result
