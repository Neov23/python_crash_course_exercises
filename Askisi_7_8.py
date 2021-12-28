#Άσκηση 7-8

sandwich_orders = ['philly', 'club', 'spicy']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Your {sandwich.title()} sandwich is ready for you to take.")
    finished_sandwiches.append(sandwich)

print(f"Here you go, sir! Inside the bag you'll find everything you ordered, "
      f"including:\n{finished_sandwiches}. Thank you.")

# Μπορούσα με περισσότερες σειρές και εντολές να κάνω τις τιμές στην τελευταία
# ...σειρά να φαίνονται πιο όμορφες χωρίς αγκύλες και αυτάκια
# Όμως θεώρησα πως μπορεί και να είναι περιττό
