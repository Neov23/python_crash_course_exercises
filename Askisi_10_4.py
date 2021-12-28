# Άσκηση 10-4

first_name = ''
last_name = ''

while first_name != 'quit':
    first_name = input('Enter your first name: (to exit, enter "quit"): ')
    if first_name == 'quit':
        break
    else:
        last_name = input('Enter your last name: ')
        print(f"Hello {first_name.title()} {last_name.title()}!")

    with open('guest_book.txt', 'a') as guest_book_file:
        guest_book_file.write(f"{first_name.title()} {last_name.title()}\n")
