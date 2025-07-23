def make_album(title, artist, songs=None):
    album = {'title': title, 'artist': artist}

    if songs:
        album['songs'] = songs
    
    return album


album_01 = make_album('Thriller', 'Michael Jackson')
print(album_01)
album_02 = make_album('Sgt. Pepper\'s Lonely Hearts Club Band', 'Beatles')
print(album_02)
album_03 = make_album('Lemonade','Beyoncé',12)
print(album_03)
album_04 = make_album('Back to Black','Amy Winehouse',12)
print(album_04)