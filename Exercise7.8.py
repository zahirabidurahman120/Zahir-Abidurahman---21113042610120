sandwich_orders = ["tuna", "chicken", "beef", "egg"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"Saya telah membuat sandwich {sandwich} Anda.")

    finished_sandwiches.append(sandwich)

print("\nDaftar sandwich yang telah dibuat:")

for sandwich in finished_sandwiches:
    print(sandwich)