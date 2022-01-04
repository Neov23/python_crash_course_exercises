# Exercise 9-12

import admin_and_privileges as a_p

# Create an admin instance from "a_p" module
neo = a_p.Admin('dimitris', 'ch', 27, 'male')

# Create and store a privileges list in instance's privileges
neo_privileges = ['You can fly', 'You are invincible', 'You can ban everybody']
neo.privileges.privileges = neo_privileges

# Call method to display instance's privileges
neo.privileges.show_privileges()