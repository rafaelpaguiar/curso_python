def city_country(city,country):
    return f"{city.title() }, {country.title()}" 

test_01 = city_country('santiago', 'chile')
print(test_01)
test_02 = city_country('diadema', 'brazil')
print(test_02)
test_03 = city_country('paris', 'france')
print(test_03)