rivers = {
    'Brasil': 'Amazonas',
    'Egito': 'Nilo',
    'China': 'Yangtzé',
    'Estados Unidos': 'Mississippi-Missouri',
    }

for country, river in rivers.items():
    print(f"O {river} atrassa o {country}")

print("\nLista de países:")
for country in rivers.keys():
    print(country)

print("\nLista de rios:")
for country in rivers.values():
    print(country)