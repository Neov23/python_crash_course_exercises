# Exercise 9-2

class Restaurant:
    """Modelization of a Restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type of Restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe Restaurant"""
        print(f"The Restaurant's name is {self.restaurant_name.title()}.")
        print(f"The cuisine type of this Restaurant is {self.cuisine_type}.")

    def open_restaurant(self):
        """Simulate the opening of the Restaurant"""
        print(f"{self.restaurant_name.title()} is now open!")

# Create an instance
hg_burger = Restaurant('heartattack grill burger', 'fast-food')

# Display the two attributes of the instance
print(f"hg_burger.restaurant_name: \n"
      f"{hg_burger.restaurant_name.title()} \n")
print(f"hg_burger.cuisine_type: \n"
      f"{hg_burger.cuisine_type} \n")

# Call two methods of the instance
print("hg_burger.describe_restaurant:")
hg_burger.describe_restaurant()
print("\nhg_burger.open_restaurant:")
hg_burger.open_restaurant()

# Exercise 9-2 below
print("\n\nExercise 9-2 below: \n")

# Create three instances from class Restaurant
o_giros_tou_thoma = Restaurant('o giros tou thoma', 'grill')
varoulko = Restaurant('varoulko', 'fish tavern')
burger_ap = Restaurant('burger ap', 'fast-food')

# Call "describe_restaurant" method for all three instances
o_giros_tou_thoma.describe_restaurant()
print("")
varoulko.describe_restaurant()
print("")
burger_ap.describe_restaurant()