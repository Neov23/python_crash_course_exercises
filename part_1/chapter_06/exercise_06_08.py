# Exercise 6-8

pets = []

rex = {
    'animal': 'dog',
    'owner': 'michael'
    }

pets.append(rex)

lily = {
    'animal': 'cat',
    'owner': 'jimmy'
    }

pets.append(lily)

zeus = {
    'animal': 'rabbit',
    'owner': 'thomas'
    }

pets.append(zeus)

for pet in pets:
    for key, value in pet.items():
        print(f"{key.title()}: {value.title()}")
    print("")