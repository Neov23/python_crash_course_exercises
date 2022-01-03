# Exercise 9-14

from random import choice

# Create list with all characters available to choose
lottery_characters = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E')

# Create a winning list that will pick 4 elements of lottery_characters
winning_characters = []

while len(winning_characters) < 4:
    character = choice(lottery_characters)

    # Prevent duplication in winning_characters
    if character not in winning_characters:
        winning_characters.append(character)

# Display the four winning characters
print("Here are today's winning numbers and/or letters:")

for character in winning_characters:
    print(character)