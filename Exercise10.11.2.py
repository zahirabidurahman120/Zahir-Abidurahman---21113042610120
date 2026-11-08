import json
from pathlib import Path

path = Path("favorite_number.json")

contents = path.read_text()
angka = json.loads(contents)

print(f"I know your favorite number! It's {angka}.")