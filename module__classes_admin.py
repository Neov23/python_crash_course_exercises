# Module: 'class': 'User' (imported), 'Admin', 'Privileges'

import module__class_user as cl_user

class Admin(cl_user.User):
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
