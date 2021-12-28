#Άσκηση 5-10

current_users = ['Adam', 'Eve', 'TAKis', 'maKIs', 'lakiS']
new_users = ['ADAM', 'Neo', 'LuNa', 'Rizla', 'takis']

current_users = [current_user.lower() for current_user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users:
        print("This username is already taken. Please try a different one.")
    else:
        print("This username is available.")

