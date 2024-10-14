def sort_by_remaining_stock(items: list) -> list:
    return sorted(items, key=lambda item: item[2])