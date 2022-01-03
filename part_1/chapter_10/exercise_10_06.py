# Exercise 10-6

while True:
    try:
        x = int(input("Insert 'x' value (for x + y = z): "))
        y = int(input("Insert 'y' value (for x + y = z): "))
        break
    except:
        print("You didn't insert a number")
    continue

z = x + y
print(f"{x} + {y} = {z}")