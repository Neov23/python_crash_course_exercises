# Exercise 8-7

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