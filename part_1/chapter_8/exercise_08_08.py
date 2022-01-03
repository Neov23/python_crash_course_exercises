# Exercise 8-8

def make_album(artist_name, album_name, track_number=None):
    """Create a Dictionary to describe a music album"""
    if track_number:
        album_info = {
            'artist': artist_name.title(), 'album': album_name.title(),
            'tracks': track_number
            }
    else:
        album_info = {
            'artist': artist_name.title(), 'album': album_name.title()
            }
    return album_info

musician = make_album('travis scott', 'astroworld')
musician_2 = make_album('vasilis karras', 'tilefonise mou')
musician_3 = make_album('sakis rouvas', 'min andistekese')
musician_4 = make_album('christos dantis', 'ena tragoudi akoma', 11)

print(musician)
print(musician_2)
print(musician_3)
print(musician_4)

print("\n\nBelow is the Exercise 8-8: \n\n")

while True:
    insert_loop = input("Do you wish to enter an album's artist and title? ")

    if insert_loop.lower() != 'yes' and insert_loop.lower() != 'no':
        print("You didn't insert a valid answer. Try again.")
        continue
    elif insert_loop.lower() == 'no':
        break
    else:
        user_artist_name = input("Enter a singers name: ")
        user_album_name = input("Enter singer's album name: ")
        
        user_info = make_album(user_artist_name, user_album_name)
        print(user_info)