# Exercise 8-3

def make_shirt(size, message):
    print(f"The shirt size is {size.upper()} and there is a message printed "
          f"in front of it, saying {message.upper()}.")

make_shirt('xxl', 'never give up')
print("")
make_shirt(message='never give up', size='xxl')