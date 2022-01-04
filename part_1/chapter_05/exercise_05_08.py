# Exercise 5-8

usernames = ['neo', 'leo', 'yoda', 'tomtom', 'admin']

for username in usernames:
    if username == 'admin':
        print(f"Hello {username.title()}! Welcome Home!")
    else:
        print(f"Welcome to our page {username.title()}.")