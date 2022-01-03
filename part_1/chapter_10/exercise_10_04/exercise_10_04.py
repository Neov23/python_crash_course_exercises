# Exercise 10-4

while True:
    enter = input("Do you want to enter the program?")
    if enter.lower() != 'yes' and enter.lower() != 'no':
        print("Invalid answer, try again!")
        continue
    elif enter.lower() == 'no':
        break
    else:
        full_name = input("Enter your full name: ")
        print(f"Hello {full_name.title()}!")

    with open('guest_book.txt', 'a') as guest_book_file:
        guest_book_file.write(f"{full_name.title()}\n")