#Άσκηση 3-7 (συνέχιση από 3-6)
invites = ["vaso", "vasiliki", "maria", "michalis"]
rejected_invites = "vaso"
print(f"Τελικά η {rejected_invites.title()} δεν θα παρευρεθεί στον δείπνο για ευνόητους λόγους.\n\n")

del invites[0]
invites.append("Giorgos")
print(f"Η νέα ανανεωμένη λίστα καλεσμένων είναι η παρακάτω: \n\n1. {invites[0].title()} \n2. {invites[1].title()} \n3. {invites[2].title()} \n4. {invites[3].title()} \n")

invites.insert(0, "Takis")
invites.insert(2, "Makis")
invites.append("Lakis")

print(f"Η νέα λίστα καλεσμένων μετά την εύρεση μεγαλύτερου τραπεζιού είναι η παρακάτω: \n\n1. {invites[0].title()} \n2. {invites[1].title()}\n3. {invites[2].title()}\n4. {invites[3].title()}\n5. {invites[4].title()}\n6. {invites[5].title()} \n7. {invites[6].title()} \n")

print("Σας ενημερώνω όλους πως έχω βρει μεγαλύτερο τραπέζι για δειπνο. \n\n")

print("Νέα ανακοίνωση: \n\nΤελικά μπορώ να προσκαλέσω μόνο δύο άτομα. \n")

rejected_invites2 = invites.pop()

print(f"Αγαπητέ/ή {rejected_invites2.title()}, λυπάμαι που δεν θα σε φιλοξενήσω στο δείπνο.")

rejected_invites2 = invites.pop()

print(f"Αγαπητέ/ή {rejected_invites2.title()}, λυπάμαι που δεν θα σε φιλοξενήσω στο δείπνο.")

rejected_invites2 = invites.pop()

print(f"Αγαπητέ/ή {rejected_invites2.title()}, λυπάμαι που δεν θα σε φιλοξενήσω στο δείπνο.")

rejected_invites2 = invites.pop()

print(f"Αγαπητέ/ή {rejected_invites2.title()}, λυπάμαι που δεν θα σε φιλοξενήσω στο δείπνο.")

rejected_invites2 = invites.pop()

print(f"Αγαπητέ/ή {rejected_invites2.title()}, λυπάμαι που δεν θα σε φιλοξενήσω στο δείπνο.")

print(f"Αγαπητέ/ή {invites[0].title()}, εξακολουθείς να είσαι καλεσμένος/η στο δειπνο.")

print(f"Αγαπητέ/ή {invites[1].title()}, εξακολουθείς να είσαι καλεσμένος/η στο δειπνο.")

print(invites)

del invites[1]
del invites[0]

print(invites)
#Η άσκηση με δυσκόλεψε ελαφρώς
