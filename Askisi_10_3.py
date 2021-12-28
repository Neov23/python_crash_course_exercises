# Άσκηση 10-3

username = input('Όνομα: ')

with open('guest.txt', 'a') as guest_file:
    guest_file.write(f"{username}\n")
