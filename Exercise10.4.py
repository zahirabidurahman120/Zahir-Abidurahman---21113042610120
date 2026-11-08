from pathlib import Path

name = input("Masukkan nama Anda: ")

path = Path("guest.txt")
path.write_text(name)

print(f"Selamat datang, {name}!")