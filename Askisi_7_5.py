#Άσκηση 7-5

customer_info = "Enter your age: "
customer_info += "\nWhen you're done, type '0': "

age = ""

while  age != 0:
    age = int(input(customer_info))

    if age != 0:

        if age < 3:
            print("\nThe ticket is free for you!\n")
        elif age < 12:
            print("\nThe ticket costs $10 for you.\n")
        else:
            print("\nThe ticket costs $15 for you.\n")
