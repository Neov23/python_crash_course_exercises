# Άσκηση 9-5 (Από 9-3)

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

a1 = User('θωμάς', 'κατωγιός', 27, 'άντρας')
a2 = User('γιάννης', 'μανταλάκης', 25, 'άντρας')
a3 = User('ιωάννα', 'χριστοδούλου', 25, 'γυναίκα')

a1.describe_user()
a1.greet_user()
a2.describe_user()
a2.greet_user()
a3.describe_user()
a3.greet_user()

print("\n\nΠαρακάτω η ασκηση 9-5:\n")

hacker = User('fake', 'name', 0, 'neutral')

hacker.increment_login_attempts()
hacker.increment_login_attempts()
hacker.increment_login_attempts()
hacker.increment_login_attempts()
hacker.increment_login_attempts()

print(f'You attempted to log into your profile {hacker.login_attempts} times.')

hacker.reset_login_attempts()

print(f'You attempted to log into your profile {hacker.login_attempts} times.')
