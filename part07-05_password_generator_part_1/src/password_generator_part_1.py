import random

def generate_password(length):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length))