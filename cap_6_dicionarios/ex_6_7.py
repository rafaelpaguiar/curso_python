person_01 = {
    'first_name': 'Luide',
    'last_name': 'Matos' ,
    'age': 40,
    'city': 'Salto de Itarare',
    }

person_02 = {
    'first_name': 'Carlos',
    'last_name': 'Alberto',
    'age': 90,
    'city': 'Sao Paulo',
    }

person_03 = {
    'first_name': 'Bob',
    'last_name': 'Marley',
    'age': 45,
    'city': 'Kingstown',
    }

persons = [person_01, person_02, person_03]

for person in persons:
    print(f"First Name: {person['first_name'].title()}")
    print(f"Last Name: {person['last_name'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}\n")