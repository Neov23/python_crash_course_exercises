# Exercise 7-8

sandwich_orders = ['philly', 'club', 'spicy']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Your {sandwich.title()} sandwich is ready for you to take.")
    finished_sandwiches.append(sandwich)

print("")

print("Here you go, sir! Inside the bag you'll find everything you ordered, "
      "including:")
for sandwich in finished_sandwiches:
    print(sandwich.title())