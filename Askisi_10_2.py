# Άσκηση 10-2

filename = 'learning_python.txt'

with open(filename) as file_object:
    learn_py = file_object.readlines()

for x in learn_py:
    x = x.rstrip()
    print(x.replace('Python', 'C'))


# Το έλυσα με βοήθεια από το GitHub του Eric.
# Το έλυσα μόνος με τον παρακάτω τρόπο, αλλά για μη-εμφανή λόγο, δεν λειτούργησε

"""
filename = 'learning_python.txt'

with open(filename) as file_object:
    learn_py = file_object.readlines()

for x in learn_py:
    x = x.replace('Python', 'C')

for x in learn_py:
    print(x.rstrip())
"""

# Υποθέτω γιατί στα for, το x δουλεύει μόνο μέσα στον βρόχο, οπότε γίνεται
# replace, και μόλις τερματήσει ο βρόχος, το x δεν επιστρέφει ως νέα τιμή
