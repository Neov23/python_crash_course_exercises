# Exercise 8-12

def sandwich(*toppings):
    print("\nWe will create your sandwich with the following toppings:")
    for topping in toppings:
        print(f"-{topping.title()}")

sandwich('aeros', 'kaseri', 'feta', 'ntomata')
sandwich('feta', 'elia', 'ntomata')
sandwich('galopoula', 'kaseri')