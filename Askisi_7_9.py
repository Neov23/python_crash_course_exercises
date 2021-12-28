#Άσκηση 7-9 (από 7-8)

sandwich_orders = ['pastrami', 'philly', 'pastrami', 'club', 'spicy', 'pastrami']
finished_sandwiches = []

print("Sorry, delicatesen is out of Pastrami.\n")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich == 'pastrami':
        print(f"Sorry, delicatesen is out of {sandwich.title()}.")
    else:
        print(f"Your {sandwich.title()} sandwich is ready for you to take.")
        finished_sandwiches.append(sandwich)

print(f"\nHere you go, sir! Inside the bag you'll find everything you ordered, "
      f"including:\n{finished_sandwiches}. Thank you.")
print(sandwich_orders)
