# Exercise 10-5

while True:
    """Append a string to .txt file, each loop."""
    enter = input("Do you want to enter the program? ")
    if enter.lower() != 'yes' and enter.lower() != 'no':
        print("Invalid answer! Try again!")
        continue
    elif enter.lower() == 'no':
        break
    elif enter.lower() == 'yes':
        reason = input("Write a reason you love programming: ")
        with open('reasons_to_love_programming.txt', 'a') as reasons:
            reasons.write(f"I love programming because {reason}\n")