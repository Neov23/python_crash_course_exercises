#Άσκηση 4-10 (Από 4-7)

digits = []
for x in range(3, 31, 3):
    digits.append(x)
    print(x)

print(f"\nThe first three numbers of this list are: {digits[:3]}")
print(f"\nThe two numbers of the middle of this list are: {digits[4:6]}")
print(f"\nThe last three numbers of this list are: {digits[-3:]}")

#Σωστή μεν, αλλά έπρεπε manually να υπολογίσω ποιοί ειναι οι αριθμοί που
#...πρέπει να διαλέξω ως "3 middle of the list". Δεν γνωρίζω κάποια εντολή
#...που τα επιλέγει αυτόματα με βάση υπολογισμούς που πράττει.

#TIP: Σκέφτηκα πως σε μεγάλες τέτοιες λίστες, θα βοηθούσε το len()
#Π.χ. print(len(digits)) αν τυπώσει 589, κάνουμε 589/2, δηλαδή 294.5
#Άρα η μέση είναι το 295, οπότε βρίσκω πως "3 middle of the list" είναι
#digits[294:297] για να εμφανίσει 294,295,296

#Περίπλοκος τρόπος λόγω μαθηματικών, αλλά είναι ο καλύτερος που γνωρίζω ως τώρα
