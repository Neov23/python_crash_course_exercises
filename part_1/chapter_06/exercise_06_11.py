# Exercise 6-11

cities = {
    'thessaloniki': {
        'country': 'greece',
        'population': 1_000_000,
        'fact': 'They have the best souvlaki'
        },

    'frankfurt': {
        'country': 'germany',
        'population': 750_000,
        'fact': 'They have the best sausages'
        },
    
    'texas': {
        'country': 'USA',
        'population': 29_000_000,
        'fact': 'They have the best burgers'
        }
    }

for city, info in cities.items():
    print(f"{city.title()}:\n")
    country = info['country'].title()
    population = info['population']
    fact = info['fact']
    print(f"Country: {country} \nPopulation: {population} \nFact: {fact}\n\n")