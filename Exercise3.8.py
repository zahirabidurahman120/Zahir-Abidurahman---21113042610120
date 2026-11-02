places = [
    "Jepang",
    "Swiss",
    "Korea Selatan",
    "Turki",
    "Norwegia"
]

# Menampilkan urutan asli
print("Urutan asli:")
print(places)

# Mengurutkan secara alfabetis tanpa mengubah list asli
print("\nUrutan alfabetis:")
print(sorted(places))

print("\nUrutan asli setelah sorted():")
print(places)

# Mengurutkan secara alfabetis terbalik
print("\nUrutan alfabetis terbalik:")
print(sorted(places, reverse=True))

print("\nUrutan asli kembali:")
print(places)

# Membalik urutan list
places.reverse()
print("\nSetelah reverse pertama:")
print(places)

# Mengembalikan ke urutan awal
places.reverse()
print("\nSetelah reverse kedua:")
print(places)

# Mengurutkan secara alfabetis secara permanen
places.sort()
print("\nSetelah sort alfabetis:")
print(places)

# Mengurutkan secara alfabetis terbalik secara permanen
places.sort(reverse=True)
print("\nSetelah sort terbalik:")
print(places)