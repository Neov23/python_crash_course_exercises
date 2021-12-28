#Άσκηση 4-8

cubes = []
for x in range(1,11):
    cubes.append(x**3)

print(cubes)
    


#Ή διαφορετικά:

cubes = [x**3 for x in (range(1,11))]
print(cubes)
