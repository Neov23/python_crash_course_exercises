# Άσκηση 10-5

reason = ''

with open('reasons_to_love_programming.txt', 'a') as reasons_file:
            reasons_file.write("Below we see reasons people love programming:"
                               "\n\n")

while reason != 'quit':            
    reason = input('Type a reason to love programming: (to quit, type '
                   '"quit"): ')  
    if reason == 'quit':
        break   
    else:
        with open('reasons_to_love_programming.txt', 'a') as reasons_file:
            reasons_file.write(f"-{reason}\n")
