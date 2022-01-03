# Exercise 9-4

class Restaurant:
    """Modelization of a Restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type of Restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe Restaurant"""
        print(f"The Restaurant's name is {self.restaurant_name.title()}.")
        print(f"The cuisine type of this Restaurant is {self.cuisine_type}.")

    def open_restaurant(self):
        """Simulate the opening of the Restaurant"""
        print(f"{self.restaurant_name.title()} is now open!")

    def set_number_served(self, customers):
        """Set value for served customers"""
        self.number_served = customers

    def increment_number_served(self, increment):
        """Set value that will be added to number_served value"""
        self.number_served += increment

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

# Exercise 9-4 below
print("\n\nExercise 9-4 below: \n")

# Create instance "restaurant"
restaurant = Restaurant("john's pizza", 'pasta')

# Display number of served customers for "restaurant" instance
print("restaurant.number_served:")
print(restaurant.number_served)

# Change restaurant.number_served value and display again the served number
restaurant.number_served = 10
print("restaurant.number_served (after changing value to 10):")
print(restaurant.number_served)

# Call restaurant.set_number_served and display again the served number
restaurant.set_number_served(12)
print("restaurant.number_served (after calling set_number_served(12)):")
print(restaurant.number_served)

# Call method to increment the number of served customers
# Display the total number of served customers
restaurant.increment_number_served(11)
print("restaurant.number_served (after calling increment_number_served(11)):")
print(restaurant.number_served)