from pathlib import Path

path = Path("alice.txt")

try:
    contents = path.read_text(encoding="utf-8")

    jumlah_the = contents.lower().count("the")
    jumlah_the_spasi = contents.lower().count("the ")

    print("Jumlah kata/teks 'the':", jumlah_the)
    print("Jumlah teks 'the ':", jumlah_the_spasi)

except FileNotFoundError:
    print("File alice.txt tidak ditemukan.")