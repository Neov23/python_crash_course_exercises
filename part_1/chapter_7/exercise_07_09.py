# Exercise 7-9

print("Deli has run out of pastrami.\n")

sandwich_orders = ['philly', 'pastrami', 'pastrami', 'club', 'spicy', 
'pastrami']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich != 'pastrami':
        print(f"Your {sandwich.title()} sandwich is ready for you to take.")
        finished_sandwiches.append(sandwich)

print("")

print("Here you go, sir! Inside the bag you'll find everything you ordered, "
      "including:")
for sandwich in finished_sandwiches:
    print(sandwich.title())