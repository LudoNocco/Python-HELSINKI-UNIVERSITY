def filter_forbidden(string: str, forbidden: str) -> str:
    return "".join([char for char in string if char not in forbidden])