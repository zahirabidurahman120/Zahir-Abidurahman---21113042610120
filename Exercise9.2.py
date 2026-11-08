class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} menyajikan {self.cuisine_type}")


restaurant1 = Restaurant("Warung Padang", "Masakan Padang")
restaurant2 = Restaurant("Pizza Hut", "Pizza")
restaurant3 = Restaurant("Mie Ayam Pak Budi", "Mie Ayam")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()