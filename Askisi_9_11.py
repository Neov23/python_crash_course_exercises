# Άσκηση 9-11

import module__classes_user as cl_user

neo = cl_user.Admin('thomas', 'katogios', 27, 'male')
neo_privileges = ['You can fly', 'You are invincible', 'You can ban everybody']
neo.privileges.privileges = neo_privileges
neo.privileges.show_privileges()
