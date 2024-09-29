import random
import string

def generate_strong_password(length: int, include_numbers: bool, include_special: bool):
    lowercase = string.ascii_lowercase
    numbers = string.digits if include_numbers else ''
    special = "!?=+-()#" if include_special else ''
    
    all_characters = lowercase + numbers + special
    password = [random.choice(lowercase)]  # ensure at least one lowercase letter
    
    if include_numbers:
        password.append(random.choice(numbers))  # ensure at least one number
    if include_special:
        password.append(random.choice(special))  # ensure at least one special character
    
    while len(password) < length:
        password.append(random.choice(all_characters))
    
    random.shuffle(password)
    return ''.join(password)