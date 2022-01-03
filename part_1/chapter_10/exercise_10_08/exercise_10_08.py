# Exercise 10-8

filename = 'cat.txt'

try:
    """Read and display all cat names from 'cat.txt'"""
    with open(filename) as cats:
        print("Cat names:")
        for cat in cats.readlines():
            print(cat.title().rstrip())
        print("")

except FileNotFoundError:
    print(f"The following file is missing: '{filename}'.\n\n")

filename = 'dog.txt'

try:
    """Read and display all dog names from 'dog.txt'"""
    with open(filename) as dogs:
        print("Dog names:")
        for dog in dogs.readlines():
            print(dog.title().rstrip())

except FileNotFoundError:
    print("The following file is missing: '{filename}'.")