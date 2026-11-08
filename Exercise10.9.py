from pathlib import Path

files = ["cats.txt", "dogs.txt"]

for filename in files:
    path = Path(filename)

    try:
        contents = path.read_text()
        print(f"\nIsi file {filename}:")
        print(contents)

    except FileNotFoundError:
        pass