# Άσκηση 10-6 και 10-7
# Λύνοντας την 10-6, κατέληξα να έχω λυμένη και την 10-7

while True:
    try:
        x = int(input("Insert 'x' value (for x/y = z): "))
        break
    except:
        print("You didn't insert a number")
    continue

while True:
    try:
        y = int(input("Insert 'y' value (for x/y = z): "))
        break
    except:
        print("You didn't insert a number")
    continue

res = x + y
print(f"{x} + {y} = {res}")


# Λύνοντας μόνο την 10-6...
# Αφού με πήρε 20 λεπτά να λύσω την άσκηση, έλεγξα τη λύση στου Eric το GitHub
# Προσπάθησα και εγώ να το λύσω με τον τρόπο του, αλλά απέτυχα, διότι...
# ...δεν ήξερα πως έπρεπε να βάλω 'x = int(x)', και έβαζα 'x = int()'
# Παρακάτω είναι η λύση του, που ειχα την ίδια, απλώς με την παραπάνω διαφορά

"""
try:
    x = input("Give me a number: ")
    x = int(x)

    y = input("Give me another number: ")
    y = int(y)
except ValueError:
    print("Sorry, I really needed a number.")
else:
    sum = x + y
    print(f"The sum of {x} and {y} is {sum}.")
"""
