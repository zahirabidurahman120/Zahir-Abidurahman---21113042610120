import json
from pathlib import Path

path = Path("favorite_number.json")

angka = int(input("Masukkan angka favorit Anda: "))

contents = json.dumps(angka)
path.write_text(contents)

print("Angka favorit berhasil disimpan.")