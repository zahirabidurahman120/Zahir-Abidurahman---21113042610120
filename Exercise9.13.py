from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


die6 = Die()

print("Dadu 6 sisi:")
for i in range(10):
    die6.roll_die()


die10 = Die(10)

print("Dadu 10 sisi:")
for i in range(10):
    die10.roll_die()


die20 = Die(20)

print("Dadu 20 sisi:")
for i in range(10):
    die20.roll_die()