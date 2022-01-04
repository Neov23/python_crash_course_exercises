# admin_and_privileges module

from user import User

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
        """Show admin's privileges"""
        print("An admin, compared to a regular user, has the following "
              "privileges: \n")
        for privilege in self.privileges:
            print(privilege)