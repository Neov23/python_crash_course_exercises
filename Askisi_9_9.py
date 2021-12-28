# Άσκηση 9-9

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, manufacturer, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self, set_size):
        """Check battery size. If size not given value, change size to 100."""
        if set_size == False:
            self.battery_size = 100
        else:
            self.battery_size = set_size


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\nΑπό εδώ και κάτω, το output της άσκησης 9-9:\n")

my_design = ElectricCar('thomas katogios', 'the one', 2021)
my_design.battery
my_design.battery.get_range()

my_design.battery.upgrade_battery(0)
my_design.battery.get_range()

my_design.battery.upgrade_battery(75)
my_design.battery.get_range()

my_design.battery.upgrade_battery(100)
my_design.battery.get_range()
