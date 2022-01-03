# Exercise 6-9

favorite_places = {
    'dimitris': ['santorini', 'norway', 'kastoria'],
    'stella': ['santorini', 'disneyland'],
    'vasiliki': ['america', 'sweden']
    }

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places to visit are:")
    for place in places:
        print(f"-{place.title()}.")
    print("")