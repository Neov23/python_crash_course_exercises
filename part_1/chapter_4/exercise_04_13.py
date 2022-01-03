# Exercise 4-13

basic_foods = ('crepe', 'eggs', 'marmelade', 'oatmeal', 'milk')

print("Tuple:")
for food in basic_foods:
    print(food.title())

#Η λάθος εντολή που ζητάει η άσκηση είναι:
#breakfasts[3] = ('toast')

print("")

# Make a mistake on purpose by trying to modify one element of the tuple
# del basic_foods[3]

# Rewrite the tuple and use "for" loop to display each element in new tuple
basic_foods = ('crepe', 'eggs', 'honey', 'toast', 'milk')

print("New tuple:")
for food in basic_foods:
    print(food.title())