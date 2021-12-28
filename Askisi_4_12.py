#Άσκηση 4-12 (Από foods.py του βιβλίου)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#Εδώ αρχίζει η 4-12

print("\n\n")
for my_food in my_foods:
    print(f"I like {my_food.title()}")

print("")
for friend_food in friend_foods:
    print(f"My friend likes {friend_food.title()}")
