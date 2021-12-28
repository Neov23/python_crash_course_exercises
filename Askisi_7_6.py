#Άσκηση 7-6 (Από 7-4)

# Εκδοχή 1η
# Να σταματήσω το loop 'while' με υπό συνθήκη έλεγχο
# Προσοχή, μην μπερδευτείς. Για exit, γράφεις 3 φορές 'done'
# Γιατί έχω τριπλογράψει το πρόγραμμα, αφού εχει 3 εκδοχές

pizza_toppings = "Insert a pizza topping."
pizza_toppings += "\nWhen you're done, type 'done': "

answer = ""
while answer != 'done':
    answer = input(pizza_toppings)
    
    if answer != 'done':
        print(f"\n{answer.title()} has been successfully added to your pizza.\n")

print("\nYour pizza is ready!")

# Μάλλον είναι όπως το έλυσα στην 7-4 (ήδη έτοιμο)
# Η συνθήκη True είναι όλες οι τιμές εκτός του 'done'
# Άμα γράψει 'done', θα διαβάσει False και θα σταματήσει ο βρόχος

#

# Εκδοχή 2η
# Να σταματήσω το loop 'while' με μεταβλητή 'active'

pizza_toppings = "Insert a pizza topping."
pizza_toppings += "\nWhen you're done, type 'done': "

active = True
while active:
    answer = input(pizza_toppings)
    
    if answer == 'done':
        active = False
    else:
        print(f"\n{answer.title()} has been successfully added to your pizza.\n")

print("\nYour pizza is ready!")

# Έγινε σωστά η 2η εκδοχή

#

# Εκδοχή 3η
# Να σταματήσω το loop 'while' με την εντολή 'break'

pizza_toppings = "Insert a pizza topping."
pizza_toppings += "\nWhen you're done, type 'done': "

while True:
    answer = input(pizza_toppings)
    
    if answer == 'done':
        break
    else:
        print(f"\n{answer.title()} has been successfully added to your pizza.\n")

print("\nYour pizza is ready!")

# Έγινε σωστά η 3η εκδοχή
