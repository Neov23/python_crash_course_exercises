# Exercise 7-5

age = ""

while  True:
    age = input("Enter your age. When you're done, type 'done': ")
    if age == 'done':
        break

    age = int(age)
        
    if age < 3:
        print("\nThe ticket is free for you!\n")
    elif age <= 12:
        print("\nThe ticket costs $10 for you.\n")
    else:
        print("\nThe ticket costs $15 for you.\n")