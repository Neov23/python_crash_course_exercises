# Άσκηση 9-6 ('class Restaurant' από άσκηση 9-4)

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

class IceCreamStand(Restaurant):
    """Modelization of IceCreamStand, with parent-class 'Restaurant'"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type of IceCreamStand"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def flavor_list(self):
        """Show flavors"""
        print("You picked the following ice cream flavors:\n")
        for x in self.flavors:
            print(f"-{x.title()}")

my_flavors = IceCreamStand('the neighbor', 'ice cream')
my_flavors.flavors = ['chocolate', 'straciatella', 'nutella']
my_flavors.flavor_list()
