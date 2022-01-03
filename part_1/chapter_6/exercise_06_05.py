# Exercise 6-5

rivers = {'nile': 'egypt', 'aliakmonas': 'greece', 'yenisei': 'russia'}

# Display a sentence about each river and its country
print("Use a loop to print a sentence about each river:")
for river, country in rivers.items():
    print(f"The famous river {river.title()} runs through {country.title()}.")

print("")

# Display the name of each river in the dictionary
print("Use a loop to print the name of each river in the dictionary:")
for river in rivers:
    print(river.title())

print("")

# Display the name of each country in the dictionary
print("Use a loop to print the name of each country in the dictionary:")
for country in rivers.values():
    print(country.title())