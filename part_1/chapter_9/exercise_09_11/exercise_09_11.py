# Exercise 9-11

import user

# Create instance from "classes_user" module
neo = user.Admin('dimitris', 'ch', 27, 'male')

# Create and store privileges in the instance
neo_privileges = ['You can fly', 'You are invincible', 'You can ban everybody']
neo.privileges.privileges = neo_privileges

# Call method that displays instance's privileges
neo.privileges.show_privileges()