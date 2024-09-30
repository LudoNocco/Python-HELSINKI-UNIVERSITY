# string_helper module
def change_case(orig_string: str):
    return orig_string.swapcase()

def split_in_half(orig_string: str):
    midpoint = len(orig_string) // 2
    return (orig_string[:midpoint], orig_string[midpoint:])

def remove_special_characters(orig_string: str):
    return ''.join(c for c in orig_string if c.isalnum() or c.isspace())
