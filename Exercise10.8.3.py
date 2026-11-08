from pathlib import Path

files = ["Exercise10.8.1.txt", "Exercise10.8.2.txt"]

for filename in files:
    path = Path(filename)

    try:
        contents = path.read_text()
        print(f"\nIsi file {filename}:")
        print(contents)

    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")