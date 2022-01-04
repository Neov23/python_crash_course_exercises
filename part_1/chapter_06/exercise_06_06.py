# Exercise 6-6

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

must_included_members = ['jen', 'takis', 'makis', 'phil']

for name in must_included_members:
    if name in favorite_languages:
        print(f"Thank you {name.title()} for participating in our study.")
    else:
        print(f"Dear {name.title()}, you're invited to participate in our "
              f"study.")