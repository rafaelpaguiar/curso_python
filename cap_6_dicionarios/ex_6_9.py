favorite_places = {
    'rafael': ['paris', 'ilha bela'],
    'rachel:': ['toledo', 'diadema', 'amsterdam'],
    'vanessa': ['sao paulo', 'guaruja', 'roma'],
}

for person, places in favorite_places.items():
    print(f"{person.title()}")
    print("---------------")
    for place in places:
        print(place.title())
    print()