# Module: 'class': 'User', 'Admin', 'Privileges'

class User:
    """Take user info, show user info, greet user"""

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print(f"User info: \nFirst name: {self.first_name.title()}\n"
              f"Last name: {self.last_name.title()}\n"
              f"Age: {self.age} \nGender: {self.gender.title()}\n")

    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}!\n")

    def increment_login_attempts(self):
        """increments self.login_attemps value by one"""
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        """Resets self.login_attempts value"""
        self.login_attempts = 0
        return self.login_attempts


class Admin(User):
    """Modelize an admin user"""

    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()


class Privileges:
    """Modelize privileges"""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """Show user's privileges"""
        print("An admin, compared to a regular user, has the following "
              "privileges: \n")
        for x in self.privileges:
            print(f"-{x}")
