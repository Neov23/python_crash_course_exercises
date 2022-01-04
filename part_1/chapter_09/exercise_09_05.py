# Exercise 9-5

class User:
    """Create user"""

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        """Display user info"""
        print(f"User info: \nFirst name: {self.first_name.title()}\n"
              f"Last name: {self.last_name.title()}\n"
              f"Age: {self.age} \nGender: {self.gender.title()}\n")

    def greet_user(self):
        """Greet user"""
        print(f"Hello {self.first_name.title()} {self.last_name.title()}!\n")

    def increment_login_attempts(self):
        """increments login_attemps value by one"""
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        """Resets self.login_attempts value"""
        self.login_attempts = 0
        return self.login_attempts

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

print("\n\nExercise 9-5 below: \n")

# Create an instance of class "User"
hacker = User('fake', 'name', 0, 'neutral')

# Display default value of login attempts of the instance
print(f"Default value of hacker.login_attempts: \n{hacker.login_attempts} \n")

# Call method to simulate the incrementation of login attempts of the instance
# Display new value of login attempts
hacker.increment_login_attempts()
hacker.increment_login_attempts()
hacker.increment_login_attempts()
hacker.increment_login_attempts()
hacker.increment_login_attempts()
print(f"Value of hacker.login_attempts after calling increment_login_attempts:"
      f" \n{hacker.login_attempts} \n")

# Call method to reset the login attempts of the instance
# Display new value to login attempts
hacker.reset_login_attempts()
print(f"Value of hacker.login_attempts after calling reset_login_attempts: \n"
      f"{hacker.login_attempts}")