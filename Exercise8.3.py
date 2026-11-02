def make_shirt(size, message):
    print(f"Ukuran kaos: {size}")
    print(f"Tulisan pada kaos: {message}")

# Menggunakan positional arguments
make_shirt("L", "Keep Learning")

print()

# Menggunakan keyword arguments
make_shirt(size="M", message="Never Give Up")