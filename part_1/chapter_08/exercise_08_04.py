# Exercise 8-4

# Create make_shirt() function with two default parameters
def make_shirt(message='i love python', size='l'):
    print(f'The shirt size is {size.upper()} and there is a message printed '
          f'in front of it, saying "{message.title()}".')

make_shirt()
make_shirt(size='m')
make_shirt('i love programming', 'xxl')