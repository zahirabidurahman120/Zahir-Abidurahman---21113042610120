import json
from pathlib import Path

path = Path("user_data.json")

if path.exists():
    contents = path.read_text()
    user_data = json.loads(contents)

else:
    user_data = {}

    user_data["nama"] = input("Masukkan nama: ")
    user_data["umur"] = input("Masukkan umur: ")
    user_data["kota"] = input("Masukkan kota asal: ")

    contents = json.dumps(user_data)
    path.write_text(contents)

print("\nInformasi yang diingat:")
print("Nama:", user_data["nama"])
print("Umur:", user_data["umur"])
print("Kota:", user_data["kota"])