#Άσκηση 6-7 (Από 6-1)

people = {
    'my sister': {
        'first_name': 'vasiliki',
        'last_name': 'ch',
        'age': 16,
        'city': 'thessaloniki'
        },

    'my father': {
        'first_name': 'michalis',
        'last_name': 'ch',
        'age': 48,
        'city': 'thessaloniki'
        },

    'my mother': {
        'first_name': 'maria',
        'last_name': 'ch',
        'age': 50,
        'city': 'thessaloniki'
        }
    }

for name, info in people.items():
        print(f"{name.title()}'s info:\n")
        full_name = f"{info['first_name']} {info['last_name']}"
        age = info['age']
        city = info['city']

        print(f"\tFull name: {full_name.title()}")
        print(f"\tAge: {age}")
        print(f"\tCity: {city.title()}")
        print("\n")
