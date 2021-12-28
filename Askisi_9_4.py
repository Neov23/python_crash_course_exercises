# Άσκηση 9-4 (Από 9-1)

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
        """Set value that will be added to customers value"""
        self.number_served += increment

hgb = Restaurant('heartattack grill burger', 'fast-food')

print(f"Εμφανίζω την ιδιότητα του ονόματος εστιατορίου:\n"
      f"{hgb.restaurant_name.title()}\n")
print(f"Εμφανίζω την ιδιότητα του τύπου εστιατορίου:\n"
      f"{hgb.cuisine_type}\n")

hgb.describe_restaurant()
print("")
hgb.open_restaurant()

#Παρακάτω η εφαρμογή της άσκησης 9-4

print("\n\nΠαρακάτω η άσκηση 9-4:\n")

restaurant = Restaurant("john's pizza", 'pasta')

print(f'We have currently served "{restaurant.number_served}" customers.')

restaurant.number_served = 10

print(f'We have currently served "{restaurant.number_served}" customers.')

restaurant.set_number_served(12)

print(f"The last 8 hours, we've served a total number of "
      f"'{restaurant.number_served}' customers.")

restaurant.increment_number_served(11)

print(f"The total amount of served customers for the whole day is "
      f"'{restaurant.number_served}' people.")

# Δοκίμασα να κανω announcement = f'We have currently...' και μετά να γράφω απλώς
# print(announcement), αλλά φαίνεται να μην αλλάζει η μεταβλητή της ιδιότητας
# restaurant.number_served. Οπότε αναγκαστικά κάθε φορά έκανα το ίδιο print
