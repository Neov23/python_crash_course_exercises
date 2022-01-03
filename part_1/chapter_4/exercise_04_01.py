# Exercise 4-1

favorite_pizzas = ['pepperoni', 'margarita', 'special']

# Display each element of the list (one line for one element)
for pizza in favorite_pizzas:
    print(pizza.title())

print("")

# Display one sentence for each element of the list (one line for one element)
for pizza in favorite_pizzas:
    print(f"I love {pizza.title()}!")

# Display a sentence outside of the loop
print("\nI love pizza so much!")