from city_functions import city_country

def test_city_country():
    city_country_result = city_country('santiago', 'chile')
    assert city_country_result == 'Santiago, Chile'

def test_city_country_population():
    city_country_result = city_country('santiago', 'chile', '5000000')
    assert city_country_result == 'Santiago, Chile - population 5000000'