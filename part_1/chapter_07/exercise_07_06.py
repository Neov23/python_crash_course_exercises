# Exercise 7-6

# Version 1: Use a conditional check in "while" loop to stop the look
print("Version 1: \n")

answer = ""

while answer != 'quit':
    answer = input("Insert a pizza topping. \nWhen you're done, type 'quit': ")
    
    if answer != 'quit':
        print(f"\n{answer.title()} has been successfully added to your "
              f"pizza.\n")

print("\nYour pizza is ready!\n\n")

# Version 2: Use a variable "active" to check how long the loop will run
print("Version 2: \n")

answer = ""
active = 0

while answer != 'quit':
    active += 1
    answer = input("Insert a pizza topping. \nWhen you're done, type 'quit': ")
    
    if answer != 'quit':
        print(f"\n{answer.title()} has been successfully added to your "
              f"pizza.\n")

print("\nYour pizza is ready!")
print(f"The loop ran {active} times.\n\n")

# Version 3: Use "break" to exit the loop when user input is "quit"
print("Version 3: \n")

answer = ""

while True:
    answer = input("Insert a pizza topping. \nWhen you're done, type 'quit': ")
    
    if answer != 'quit':
        print(f"\n{answer.title()} has been successfully added to your "
              f"pizza.\n")
    else:
        break

print("\nYour pizza is ready!")