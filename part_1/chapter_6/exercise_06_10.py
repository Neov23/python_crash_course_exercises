# Exercise 6-10

favorite_numbers = {
    'takis': [5, 6, 7],
    'makis': [10, 11, 12],
    'lakis': [15, 16, 17],
    'sakis': [20, 21, 22, 23],
    'mitsos': [3, 23, 26]
    }

for names, numbers in favorite_numbers.items():
    print(f"{names.title()}'s favorite numbers are: ")
    for number in numbers:
        print(f"{number}")
    print("")