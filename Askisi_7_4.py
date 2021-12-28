#Άσκηση 7-4

pizza_toppings = "Insert a pizza topping."
pizza_toppings += "\nWhen you're done, type 'done': "

answer = ""
while answer != 'done':
    answer = input(pizza_toppings)
    
    if answer != 'done':
        print(f"\n{answer.title()} has been successfully added to your pizza.\n")

print("\nYour pizza is ready!")
