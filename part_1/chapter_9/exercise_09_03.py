# Exercise 9-3

class User:
    """Create user"""

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        """Display user info"""
        print(f"User info: \nFirst name: {self.first_name.title()}\n"
              f"Last name: {self.last_name.title()}\n"
              f"Age: {self.age} \nGender: {self.gender.title()}\n")

    def greet_user(self):
        """Greet user"""
        print(f"Hello {self.first_name.title()} {self.last_name.title()}!\n")

# Create three instances (users)
ch = User('dimitris', 'ch', 27, 'male')
mantalaki = User('johanna', 'mantalaki', 25, 'female')
cena = User('john', 'cena', 44, 'male')

# Greet all three users and display their info
ch.greet_user()
ch.describe_user()
print("")

mantalaki.greet_user()
mantalaki.describe_user()
print("")

cena.greet_user()
cena.describe_user()