# Exercise 10-1

"""Display each line in learning_python.txt, 3 times, with different methods"""

filename = 'learning_python.txt'

# Method 1
with open(filename) as file_object:
    print(file_object.read())

# Method 2
with open(filename) as file_object:
    for line in file_object.readlines():
        print(line.rstrip())
    print("")

# Method 3
with open(filename) as file_object:
    textlines = file_object.readlines()
    
for line in textlines:
    print(line.rstrip())