pet_01 = {
    'name': 'Pepe',
    'specie': 'dog',
    'owner': 'Rachel',
    }

pet_02 = {
    'name': 'Charlote',
    'specie': 'cat',
    'owner': 'Vanessa',
    }

pet_03 = {
    'name': 'Dourado',
    'specie': 'Fish',
    'owner': 'Rafael',
    }

pets = [pet_01, pet_02, pet_03]

for pet in pets:
    print(f"{pet['name'].title()} is a {pet['specie'].title()} and it's owner is {pet['owner'].title()}")