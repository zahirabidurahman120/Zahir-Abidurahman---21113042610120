from pathlib import Path

path = Path("learning_python.txt")

contents = path.read_text()

print("Membaca seluruh isi file:")
print(contents)

print("Membaca menggunakan list:")
lines = contents.splitlines()

for line in lines:
    print(line)