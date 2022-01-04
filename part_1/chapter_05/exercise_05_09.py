# Exercise 5-9 (from 5-8)

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username.title()}! Welcome Home!")
        else:
            print(f"Welcome to our page {username.title()}.")
else:
    print("We need to find some users.")