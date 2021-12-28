#Άσκηση 3-5
invites = ["vaso", "vasiliki", "maria", "michalis"]
rejected_invites = "vaso"
print(f"Τελικά η {rejected_invites.title()} δεν θα παρευρεθεί στον δείπνο για ευνόητους λόγους.\n\n")

del invites[0]
invites.append("Giorgos")
print(f"Η νέα ανανεωμένη λίστα καλεσμένων είναι η παρακάτω: \n\n1. {invites[0].title()} \n2. {invites[1].title()} \n3. {invites[2].title()} \n4. {invites[3].title()}")
'''Η άσκηση ολοκληρώθηκε. Νομίζω είναι σωστή, αλλά δεν ξέρω αν έπρεπε να
χρησιμοποιήσω διαφορετικά τις εντολές del, pop, remove.'''
