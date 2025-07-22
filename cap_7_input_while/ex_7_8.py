sandwich_orders = ['Bauru', 'Bánh mì', 'Shawarma', 'Katsu Sando', 'BLT', 
                   'Croque Madame', 'Falafel', 'Cemita', 'Choripán']
finished_sandwiches =[]

while sandwich_orders:
    sandwich_ready = sandwich_orders.pop(0)
    print(f"Your {sandwich_ready} is ready!")
    finished_sandwiches.append(sandwich_ready)

print()

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
