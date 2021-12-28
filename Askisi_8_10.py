# Άσκηση 8-10 (από 8-9)

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

send_messages(short_messages)

print("\nshow_messages(short_messages):\n")
show_messages(short_messages)

print("\nshow_messages(sent_messages):\n")
show_messages(sent_messages)
