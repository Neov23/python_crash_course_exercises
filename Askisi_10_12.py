# Άσκηση 10-12 (αρχικά, το αρχειο .json δεν υπάρχει επίτηδες)
# Τρέξε το πρόγραμμα 2 φορές για να δεις πως λειτουργεί χωρίς bugs

import json

filename = 'favorite_number.json'

favorite_number = None

while True:
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        try:
            favorite_number = int(input("Insert your favorite number: "))
            with open(filename, 'w') as f:
                json.dump(favorite_number, f)
        except ValueError:
            print("You didn't insert an integer number, try again. \n")
            continue
    break

if favorite_number != None:
    print(f"I know your favorite number! It's {favorite_number}.")


'''Αρκετό nesting μέσα στο while, αλλά για να λειτουργήσει λεπτομερώς, μου
   φάνηκε απαραίτητο. Είδα μετά και την λύση του Eric στο GitHub, και το έκανε
   χωρίς λεπτομέρειες. Σε περίπτωση που έβαζε string ως fav num, θα διάβαζε
   string.'''
