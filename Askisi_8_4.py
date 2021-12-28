# Άσκηση 8-4 (από 8-3)

# default size=L

def make_shirt(message, size='l'):
    print(f"The shirt size is {size.upper()} and there is a message printed "
          f"in front of it, saying {message.title()}.")

make_shirt('i love python')
print("")

# default size=M

def make_shirt(message, size='m'):
    print(f"The shirt size is {size.upper()} and there is a message printed "
          f"in front of it, saying {message.title()}.")

make_shirt('i love python')
print("")

# default size=XXXL

def make_shirt(message, size='xxxl'):
    print(f"The shirt size is {size.upper()} and there is a message printed "
          f"in front of it, saying {message}!")

make_shirt('I love programming')
