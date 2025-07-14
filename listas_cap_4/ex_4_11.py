pizzas = ["atum", "calabresa", "portuguesa"]

for pizza in pizzas:
    print(f"Gosto de pizza de {pizza}.")
print("Eu amo pizza.\n")

friends_pizzas = pizzas[:]

pizzas.append("mussarela")
friends_pizzas.append("escarola")

for pizza in pizzas:
    print(f"Gosto de pizza de {pizza}.\n")

for pizza in friends_pizzas:
    print(f"Meu amigo gosta de pizza de {pizza}.\n")
