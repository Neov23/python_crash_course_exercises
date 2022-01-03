# Exercise 3-10

# Initialize elements in a list and display the list
favorite_foods = ['pizza', 'burger', 'gyros', 'crepe', 'cake', 'pancakes', 
'steak']
print(f"Default list: \n{favorite_foods}\n")

# Appending coffeccino to the list
favorite_foods.append('coffeccino')
print(f"Using 'list.append('coffeccino')': \n{favorite_foods} \n")

# Inserting squid in fourth place of the list
favorite_foods.insert(3, 'squid')
print(f"Using 'list.insert(3, 'squid')': \n{favorite_foods} \n")

# Deleting the fourth element of the list
del favorite_foods[3]
print(f"Using 'del list[3]': \n{favorite_foods} \n")

# Remove sixth element of the list, and add it to a second list
# Display both lists
not_favorite_foods = favorite_foods.pop(5)
print("Using 'second_list = list.pop(5)': ")
print(f"Original list: {favorite_foods} ")
print(f"Second list: {not_favorite_foods} \n")

# Remove an element of the list by name
favorite_foods.remove('coffeccino')
print(f"Using 'list.remove('coffeccino')': \n{favorite_foods} \n")

# Create a variable and use it to remove element of the list
too_casual = 'steak'
favorite_foods.remove(too_casual)
print("Created a variable 'too_casual = 'steak'' ")
print(f"Used 'list.remove(too_casual)': \n{favorite_foods} \n")

# Display alphabetical order of list, without actually editing list
# Display again the list in default order, to show nothing has changed
print("Using 'print(sorted(list))': ")
print(f"{sorted(favorite_foods)} \n")
print("Display default list to show nothing has changed: ")
print(f"{favorite_foods} \n")

# Display reverse alphabetical order of list, without actually editing list
# Display again the list in default order, to show nothing has changed
print("Using 'print(sorted(list, reverse=True))': ")
print(f"{sorted(favorite_foods, reverse=True)} \n")
print("Display default list to show nothing has changed: ")
print(f"{favorite_foods} \n")

# Reverse the list and display it
favorite_foods.reverse()
print(f"Using 'list.reverse()': \n{favorite_foods} \n")

# Reverse again the (reversed) list and display it
favorite_foods.reverse()
print(f"Using 'list.reverse()' again: \n{favorite_foods} \n")

# Sort the list in alphabetical order and display it
favorite_foods.sort()
print(f"Using 'list.sort()': \n{favorite_foods} \n")

# Sort the list in reverse alphabetical order and display it
favorite_foods.sort(reverse=True)
print(f"Using 'list.sort(reverse=True): \n{favorite_foods} \n")

# Display the number of elements in the list
print(f"Using 'len(list)': \n{len(favorite_foods)} \n")