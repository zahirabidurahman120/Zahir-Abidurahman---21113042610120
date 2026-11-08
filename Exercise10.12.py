import json
from pathlib import Path

path = Path("favorite_number.json")

if path.exists():
    contents = path.read_text()
    angka = json.loads(contents)

    print(f"I know your favorite number! It's {angka}.")

else:
    angka = int(input("Masukkan angka favorit Anda: "))

    contents = json.dumps(angka)
    path.write_text(contents)

    print("Angka favorit berhasil disimpan.")