# Pengujian string
name = "Zahir"

print(name == "Zahir")
print(name != "Zahir")

# Pengujian lower()
print(name.lower() == "zahir")
print(name.lower() == "andi")

# Pengujian angka
number = 15

print(number == 15)
print(number != 15)
print(number > 10)
print(number < 10)
print(number >= 15)
print(number <= 10)

# Pengujian and dan or
print(number > 10 and number < 20)
print(number < 10 or number > 20)

# Pengujian dalam list
foods = ["pizza", "burger", "noodles"]

print("pizza" in foods)
print("sushi" in foods)

# Pengujian tidak dalam list
print("sushi" not in foods)
print("pizza" not in foods)