guests = [
    "B.J. Habibie",
    "Albert Einstein",
    "Thomas Edison",
    "Nikola Tesla",
    "Elon Musk",
    "Isaac Newton"
]

print("Maaf, saya hanya dapat mengundang dua orang untuk makan malam.")

# Menghapus tamu sampai tersisa dua orang
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Maaf {removed_guest}, saya tidak dapat mengundang Anda.")

# Memberikan informasi kepada dua tamu yang tersisa
print("\nDua tamu yang tetap diundang:")

for guest in guests:
    print(f"Halo {guest}, Anda tetap diundang untuk makan malam.")

# Menghapus dua nama yang tersisa
del guests[0]
del guests[0]

print("\nDaftar tamu setelah dihapus:")
print(guests)