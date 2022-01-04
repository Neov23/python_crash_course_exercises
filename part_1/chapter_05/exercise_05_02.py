# Exercise 5-2

favorite_number = 23
favorite_number_string = 'TWENTY THREE'
words = ['hello', 'friend', 'programming']

# Display initial variables and lists
print(f"\nfavorite_number = {favorite_number}")
print(f"favorite_number_string = '{favorite_number_string}'")
print(f"words = {words} \n")

# Check equality and inequality in strings
print(f"Is favorite_number_string == 'TWENTY THREE'? \n"
      f"Answer: {favorite_number_string == 'TWENTY THREE'}")

print(f"Is favorite_number_string != 'TWENTY THREE'? \n"
      f"Answer: {favorite_number_string != 'TWENTY THREE'} \n")

# Check with "lower()" method
print(f"Is favorite_number_string == 'TWENTY THREE'.lower()? \n"
      f"Answer: {favorite_number_string == 'TWENTY THREE'.lower()}")

print(f"Is favorite_number_string != 'TWENTY THREE'.lower()? \n"
      f"Answer: {favorite_number_string != 'TWENTY THREE'.lower()} \n")

# Numeric check that includes equality and inequality
print(f"Is favorite_number == 23 and favorite_number < 40? \n"
      f"Answer: {favorite_number == 23 and favorite_number < 40} \n")

# Check with keywords "and" and "or"
print(f"Is favorite_number == 23 and favorite_number > 100? \n"
      f"Answer: {favorite_number == 23 and favorite_number > 100}")
print(f"Is favorite_number == 23 or favorite_number > 100? \n"
      f"Answer: {favorite_number == 23 or favorite_number > 100} \n")

# Check if an element is part of a list
print(f"Is 'hacker' in words? \nAnswer: {'hacker' in words} \n")

# Check if an element is not part of a list
print(f"Is 'hacker' not in words? \nAnswer: {'hacker' not in words} \n")