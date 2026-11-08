def make_album(artist, title, number_of_songs=None):
    album = {
        "artist": artist,
        "title": title
    }

    if number_of_songs is not None:
        album["number_of_songs"] = number_of_songs

    return album


album1 = make_album("Taylor Swift", "1989")
album2 = make_album("Ariana Grande", "Positions")
album3 = make_album("Ed Sheeran", "Divide", 16)

print(album1)
print(album2)
print(album3)