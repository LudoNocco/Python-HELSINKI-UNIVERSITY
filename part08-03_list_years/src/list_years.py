from datetime import date

def list_years(dates: list) -> list:
    list = [date.year for date in dates]
    return sorted(list) if list else list