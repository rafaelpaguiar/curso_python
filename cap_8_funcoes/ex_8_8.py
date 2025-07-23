def make_album(title, artist, songs=None):
    album = {'title': title, 'artist': artist}

    if songs:
        album['songs'] = songs
    
    return album


while True:
    print("\nLet's save a album:")
    print("(enter 'q' at any time to quit)")

    title = input("Enter album name: ")
    if title == 'q':
        break

    artist = input("Enter album artist: ")
    if title == 'q':
        break

    songs = input("Songs in this album: ") 
    if title == 'q':
        break
    if songs:
        songs = int(songs)

    album = make_album(title, artist, songs)
    print(album)