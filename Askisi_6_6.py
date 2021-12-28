#Άσκηση 6-6

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

must_included_members = ['jen', 'takis', 'makis', 'phil']

for member in must_included_members:
    if member in favorite_languages:
        print(f"\nThank you {member.title()} for participating in our study.")
    else:
        print(f"\nDear {member.title()}, you are invited to participate in our study.")

# Μέχρι στιγμής οι ασκήσεις του Κεφαλαίου 6 μου φάνηκαν σχετικά εύκολες
# Μου πήραν πολύ λίγο χρόνο να τις ολοκληρώσω
