favorite_places = {
    "zahir": ["bali", "yogyakarta", "bandung"],
    "andi": ["jakarta", "malang"],
    "budi": ["surakarta", "lombok", "bromo"]
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")

    for place in places:
        print(f"- {place.title()}")