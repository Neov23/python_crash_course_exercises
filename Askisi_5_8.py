#Άσκηση 5-8

names = ['neo', 'smith', 'kyle', 'thomas', 'admin']

for name in names:
    if name == 'admin':
        print(f"Hello {name.title()}! Welcome Home!")
    elif name in names and name != 'admin':
        print(f"Welcome to our page {name.title()}.")
