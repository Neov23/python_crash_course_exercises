# Άσκηση 9-14

from random import choice

lottery_tuple = (5, 10, 15, 20, 23, 25, 30, 35, 40, 45, 'A', 'B', 'C', 'D', 'E')

print("Here are today's winning numbers or letters: \n")
results = choice(lottery_tuple)
print(f"-{results} !")
results = choice(lottery_tuple)
print(f"-{results} !")
results = choice(lottery_tuple)
print(f"-{results} !")
results = choice(lottery_tuple)
print(f"-{results} !")
