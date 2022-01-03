# Exercise 10-12 (run the program twice, to see how it works without bugs)

import json

filename = 'favorite_number.json'
favorite_number = None

while True:
    # Open filename and load it's value into a variable
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    # If filename does not exist, create a value and store it in filename
    except FileNotFoundError:
        try:
            favorite_number = int(input("Insert your favorite number: "))
            with open(filename, 'w') as f:
                json.dump(favorite_number, f)
        # If input isn't integer, repeat loop
        except ValueError:
            print("You didn't insert an integer number, try again. \n")
            continue
    break

# Take number either from .json file, or from user input and display it
print(f"I know your favorite number! It's {favorite_number}.")