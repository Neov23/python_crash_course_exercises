# Άσκηση 10-1

filename = 'learning_python.txt'

with open(filename) as file_object:
    print(file_object.read())  

with open(filename) as file_object:
    for x in file_object.readlines():
        print(x.rstrip())

print("")

with open(filename) as file_object:
    object_list = file_object.readlines()
    
for x in object_list:
    print(x.rstrip())
