#Άσκηση 4-11 (Από 4-1)

pizzas = ['pepperoni', 'margarita', 'special']
for pizza in pizzas:
    print(f"I'm dying now for a {pizza.title()} pizza!")
print("\nI love pizza so much!")

#Η 4-11 αρχίζει εδώ

friend_pizzas = pizzas[:]
pizzas.append('nutella')
friend_pizzas.append('four cheeses')

print("\n\nMy favorite pizzas are:\n")
for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas are:\n")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())
