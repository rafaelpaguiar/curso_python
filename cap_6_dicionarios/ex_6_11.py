cities = {
    'paris': {
        'country': 'France',
        'population': 2148271,
        'fact': 'Famous for its museums.',
        } ,
    'amsterdam': {
        'country': 'Netherlands',
        'population': 933680,
        'fact': 'Famous for its coffee shops',
        } ,
    'london': {
        'country': 'England',
        'population': 8982000,
        'fact': 'Famous for its soccer teams',
        } ,
    }

for city, facts in cities.items():
    print(city.title())
    print("-----------------")
    for fact, info in facts.items():
        print(f"{fact.title()} : {info}")
