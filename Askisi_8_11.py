# Άσκηση 8-11 (από 8-9 και 8-10)

short_messages = ['geias', 'chereto', 'spera flaraki', 'gia charadan']

def show_messages(message):
    for x in message:
        print(x)

show_messages(short_messages)

print("\nΠάνω βλέπουμε το πρόγραμμα της 8-9, και από κάτω το πρόγραμμα "
      "της 8-10.\n")

# Από εδώ και κάτω ειναι η 8-10

sent_messages = []

def send_messages(message):
    while message:
        x = message.pop()
        sent_messages.append(x)
        
# Παρακάτω κάνω edit την άσκηση για να δοκιμάσω να την εφαρμόσω
# ...όπως ζητάει η 8-11

send_messages(short_messages[:])

print("\nshow_messages(short_messages):\n")

show_messages(short_messages)

print("\nshow_messages(sent_messages):\n")

show_messages(sent_messages)
