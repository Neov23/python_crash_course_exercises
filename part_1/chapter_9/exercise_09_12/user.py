# Module for Exercise 9-12

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