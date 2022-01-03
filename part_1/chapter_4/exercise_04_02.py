# Exercise 4-2

animals = ['cat', 'tiger', 'lion', 'panther']

# Display each element of the list (one line for one element)
for animal in animals:
    print(animal.title())

print("")

# Display a sentence for each element of the list (one line for one element)
for animal in animals:
    print(f"A {animal.title()} has deadly instincts.")

# Display a statement about the common characteristic of these animals
print("\nAll of these animals share the same deadly instinct.\n")