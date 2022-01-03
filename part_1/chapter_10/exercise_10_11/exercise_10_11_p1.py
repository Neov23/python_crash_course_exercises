# Exercise 10-11 (part 1)

import json

filename = 'favorite_number.json'
favorite_number = None

while favorite_number == None:
    try:
        favorite_number = int(input("Insert your favorite number: "))
    except ValueError:
        print("You didn't insert an integer number.\n")

with open(filename, 'w') as f:
    json.dump(favorite_number, f)