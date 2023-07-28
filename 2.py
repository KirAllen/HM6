import random
from lesson6 import validate_queens

def generate_positions():
    positions = list(range(1, 9))
    for i in range(4):
        random.shuffle(positions)
        while not validate_queens(positions):
            random.shuffle(positions)
        print(positions)