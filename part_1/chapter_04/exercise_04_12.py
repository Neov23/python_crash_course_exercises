# Exercise 4-12 (from "foods.py")

# foods.py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')


'''Exercise 4-12 below'''
print("\n\nExercise 4-12 below: \n")

# Display each element of my_foods with "for" loop
print("my_foods:")
for my_food in my_foods:
    print(my_food.title())

print("")

# Display each element of friend_foods with "for" loop
print("friend_foods:")
for friend_food in friend_foods:
    print(friend_food.title())