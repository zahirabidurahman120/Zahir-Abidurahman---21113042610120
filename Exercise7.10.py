responses = {}

while True:
    nama = input("Siapa nama Anda? ")
    tempat = input("Jika bisa mengunjungi satu tempat di dunia, ke mana Anda ingin pergi? ")

    responses[nama] = tempat

    ulang = input("Apakah ada orang lain yang ingin mengikuti survei? (ya/tidak): ")

    if ulang.lower() != "ya":
        break

print("\n--- HASIL SURVEI LIBURAN IMPIAN ---")

for nama, tempat in responses.items():
    print(f"{nama} ingin berlibur ke {tempat}.")