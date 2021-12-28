# Άσκηση 8-8 (από 8-7)

def make_album(name, title, track_number=None):
    if track_number:
        musician_album = {'name': name, 'title': title, 'track_number':
                          track_number}
        return musician_album
    else:
        musician_album = {'name': name, 'title': title}
        return musician_album

musician = make_album('travis scott', 'astroworld')
musician_2 = make_album('vasilis karras', 'tilefonise mou')
musician_3 = make_album('sakis rouvas', 'min andistekese')
musician_4 = make_album('christos dantis', 'ena tragoudi akoma', 
                        track_number=11)
print(musician)
print(musician_2)
print(musician_3)
print(musician_4)

while True:
    users_singer = input("Enter a singers name (if you're done, write 'done'): ")
    if users_singer == 'done':
        break
    users_album = input("Enter his/her album: ")
    users_info = make_album(users_singer, users_album)
    print(users_info)

