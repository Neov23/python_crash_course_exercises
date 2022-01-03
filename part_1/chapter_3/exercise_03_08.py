# Exercise 3-8

magic_places = ['santorini', 'norway', 'dubai', 'egypt', 'kastoria']

# Display default order of the list
print(f"Default order: \n{magic_places}\n")

'''Use functions to edit the display of the elements in the list'''
# Display elements of the list in alphabetical order
print(f"Alphabetical order with sorted(): \n{sorted(magic_places)}\n")
print(f"Default order: \n{magic_places}\n")

# Display elements of the list in reverse alphabetical order
print(f"Reverse alphabetical order with sorted('list', 'reverse=True'): \n"
      f"{sorted(magic_places, reverse=True)}\n")
print(f"Default order: \n{magic_places}\n")

'''Use functions to change elements position of the list and display list'''
# Reverse and display the list
magic_places.reverse()
print(f"Default order after list.reverse(): \n{magic_places}\n")

# Reverse and display the list again
magic_places.reverse()
print(f"Default order after list.reverse() (2nd time): \n{magic_places}\n")

# Sort and display the list
magic_places.sort()
print(f"Default order after list.sort(): \n{magic_places}\n")

# Sort the list in reverse and display it
magic_places.sort(reverse=True)
print(f"Default order after list.sort(reverse=True): \n{magic_places}\n")