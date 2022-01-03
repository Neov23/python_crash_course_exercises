# Exercise 10-3

name = input("Insert your name: ")

with open('guest.txt', 'a') as guest:
    guest.write(f"{name}\n")