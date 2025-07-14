dinner_guests = ["eistein", "mozart", "brady"]
print(f"Olá {dinner_guests[0].title()}, gostaria de jantar um dia?")
print(f"Olá {dinner_guests[1].title()}, gostaria de jantar um dia?")
print(f"Olá {dinner_guests[2].title()}, gostaria de jantar um dia?\n")
print(f"{dinner_guests[1].title()} disse que não pode jantar.\n")

dinner_guests[1] = "jordan"
print(f"{len(dinner_guests)} convidados.")
print(f"Olá {dinner_guests[0].title()}, gostaria de jantar um dia?")
print(f"Olá {dinner_guests[1].title()}, gostaria de jantar um dia?")
print(f"Olá {dinner_guests[2].title()}, gostaria de jantar um dia?\n")

print("Encontrei uma mesa maior.\n")

dinner_guests.insert(0, "marley")
dinner_guests.insert(1, "jesus")
dinner_guests.append("cury")
print(f"{len(dinner_guests)} convidados.")
print(f"Olá {dinner_guests[0].title()}, gostaria de jantar um dia?")
print(f"Olá {dinner_guests[1].title()}, gostaria de jantar um dia?")
print(f"Olá {dinner_guests[2].title()}, gostaria de jantar um dia?")
print(f"Olá {dinner_guests[3].title()}, gostaria de jantar um dia?")
print(f"Olá {dinner_guests[4].title()}, gostaria de jantar um dia?")
print(f"Olá {dinner_guests[5].title()}, gostaria de jantar um dia?\n")

print("Desculpem, a mesa só cabe dois convidados.\n")
print(f"{len(dinner_guests)} convidados.")
print(f"Desculpe {dinner_guests.pop().title()} mas terei que cancelar.")
print(f"Desculpe {dinner_guests.pop().title()} mas terei que cancelar.")
print(f"Desculpe {dinner_guests.pop().title()} mas terei que cancelar.")
print(f"Desculpe {dinner_guests.pop().title()} mas terei que cancelar.\n")

print(f"{dinner_guests[0].title()}, você continua convidado.")
print(f"{dinner_guests[1].title()}, você continua convidado.\n")
print(f"{len(dinner_guests)} convidados.")
del dinner_guests[0]
del dinner_guests[0]

print(f"Lista do convidados vazia:")
print(dinner_guests)
print(f"{len(dinner_guests)} convidados.")