# Exercise 4-11

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

'''Exercise 4-11 below'''
print("\n\nExercise 4-11 below: \n")

# Create copy of favorite_pizzas
friend_pizzas = favorite_pizzas[:]

# Add element to original list
favorite_pizzas.append('nutella')

# Add element to copied list
friend_pizzas.append('greek')

# Prove that we have two separate lists
print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())