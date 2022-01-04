# Exercise 8-11

short_messages = ['hi', 'hello', 'yo', 'sup']

def show_messages(any_list):
    """For each element of the list, print the element"""
    for element in any_list:
        print(element)

show_messages(short_messages)

# Exercise 8-11 below
print("\n\nExercise 8-11 below:")

sent_messages = []

def send_messages(any_list):
    """Transfer elements from any_list to sent_messages"""
    while any_list:
        element = any_list.pop()
        sent_messages.append(element)

send_messages(short_messages[:])

print("\nprint(short_messages):")
print(short_messages)

print("\nprint(sent_messages):")
print(sent_messages)