# Exercise 8-6

def city_country(city, country):
    return f'"{city.title()}, {country.title()}"'

city_1 = city_country('thessaloniki', 'greece')
city_2 = city_country('london', 'england')
city_3 = city_country('alexandria', 'egypt')

print(city_1)
print(city_2)
print(city_3)