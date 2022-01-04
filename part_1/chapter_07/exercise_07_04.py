# Exercise 7-4

answer = ""
while answer != 'done':
    answer = input("Insert a pizza topping. \nWhen you're done, type 'done': ")
    
    if answer != 'done':
        print(f"\n{answer.title()} has been successfully added to your "
              f"pizza.\n")

print("\nYour pizza is ready!")