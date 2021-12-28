#Άσκηση 6-5

rivers = {'nile': 'egypt', 'aliakmonas': 'greece', 'yenisei': 'russia'}

for river, country in rivers.items():
    print(f"The famous river {river.title()} runs through {country.title()}.")

print("")

for river in rivers:
    print(river.title())

print("")

for country in rivers.values():
    print(country.title())
