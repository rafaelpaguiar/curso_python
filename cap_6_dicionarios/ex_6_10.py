favorite_numbers = {
    'Anna': [2,3,4,5,6],
    'Linda': [7,8,9,0],
    'Edmund': [10,30,21,46],
    'Rafael': [33,99,2],
    'Rachel': [1029,2901920,1290912,42432],
    }


for person, favorite_number in favorite_numbers.items():
    print(person.title())
    print("Favorite numbers:")
    for number in favorite_number:
        print(number)
    print()