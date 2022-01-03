# Exericse 10-9

filename = 'cat.txt'

try:
    """Read and display all cat names from 'cat.txt'"""
    with open(filename) as cat_file:
        print("Cat names:")
        for cat in cat_file.readlines():
            print(cat.title().rstrip())
        print("")
        
except FileNotFoundError:
    pass

filename = 'dog.txt'

try:
    """Read and display all dog names from 'dog.txt'"""
    with open(filename) as dog_file:
        print("Dog names:")
        for dog in dog_file.readlines():
            print(dog.title().rstrip())

except FileNotFoundError:
    pass