# Άσκηση 8-12

def sandwich(*toppings):
    print("\n\nWe will create your sandwich with the following toppings:\n")
    for x in toppings:
        print(f"-{x.title()}")

sandwich('aeros', 'kaseri', 'feta', 'ntomata')
sandwich('feta', 'elia', 'ntomata')
sandwich('galopoula', 'kaseri')
