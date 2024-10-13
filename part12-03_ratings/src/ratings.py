def sort_by_ratings(items: list): 
    return sorted(items, key=lambda t:t["rating"], reverse=True)