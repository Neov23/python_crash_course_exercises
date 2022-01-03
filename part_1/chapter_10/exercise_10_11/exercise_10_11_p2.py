# Exercise 10-11 (part 2)

import json

filename = 'favorite_number.json'
favorite_number = None

try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    print(f"'{filename}' not found. Go to 'exercise_10_11_p1.py' and run it")

if favorite_number != None:
    print(f"I know your favorite number! It's {favorite_number}.")