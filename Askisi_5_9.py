#Άσκηση 5-9

names = []

if names:
    for name in names:
        if name == 'admin':
            print(f"Hello {name.title()}! Welcome Home!")
        elif name in names and name != 'admin':
            print(f"Welcome to our page {name.title()}.")
else:
    print("We need to find some users")
