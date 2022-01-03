# Exercise 5-10

current_users = ['Adam', 'Eve', 'TAKis', 'maKIs', 'lakiS']
new_users = ['ADAM', 'Neo', 'LuNa', 'tomtom', 'takis']

# Create a copy list of current_users, but all elements are lower case
# We do not edit current_users to lower case, to keep it right for other use
current_users_lower = [current_user.lower() for current_user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} is already taken. Please try a different one.")
    else:
        print(f"{new_user} is available.")