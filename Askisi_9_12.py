# Άσκηση 9-12

import module__classes_admin as cl_admin

neo = cl_admin.Admin('thomas', 'katogios', 27, 'male')
neo_privileges = ['You can fly', 'You are invincible', 'You can ban everybody']
neo.privileges.privileges = neo_privileges
neo.privileges.show_privileges()
