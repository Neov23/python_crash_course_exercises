# Άσκηση 10-8

filename = 'cat.txt'

try:
    with open(filename) as cat_file:
        print("Cat names: \n")
        for cat in cat_file.readlines():
            print(cat.title().rstrip())
        print("\n")
        
except FileNotFoundError:
    print(f"The following file is missing: '{filename}'.\n\n")

filename = 'dog.txt'

try:
    with open(filename) as dog_file:
        print("Dog names: \n")
        for dog in dog_file.readlines():
            print(dog.title().rstrip())
        print("")

except FileNotFoundError:
    print("The following file is missing: '{filename}'.")
