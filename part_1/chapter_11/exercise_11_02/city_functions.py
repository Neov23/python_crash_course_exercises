# Module for Exercise 11-2

def city_country(city, country, population=''):
    if population:
        return f'"{city.title()}, {country.title()}. Population: {population}"'
    else:
        return f'"{city.title()}, {country.title()}"'