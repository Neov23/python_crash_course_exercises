#Άσκηση 5-11

numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")

#Δεν έγραψα στα μεμονωμένα numbers (f"{number}st") κ.λπ, για να φανεί ευανάγνωστο
