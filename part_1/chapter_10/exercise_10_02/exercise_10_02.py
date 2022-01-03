# Exercise 10-2

filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.rstrip()
    print(line.replace('Python', 'C'))