# Άσκηση 9-1

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

hgb = Restaurant('heartattack grill burger', 'fast-food')

print(f"Εμφανίζω την ιδιότητα του ονόματος εστιατορίου:\n"
      f"{hgb.restaurant_name.title()}\n")
print(f"Εμφανίζω την ιδιότητα του τύπου εστιατορίου:\n"
      f"{hgb.cuisine_type}\n")

hgb.describe_restaurant()
print("")
hgb.open_restaurant()
