pizzas = ["margherita", "pepperoni", "cheese"]

friend_pizzas = pizzas[:]

pizzas.append("bbq chicken")
friend_pizzas.append("vegetarian")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)