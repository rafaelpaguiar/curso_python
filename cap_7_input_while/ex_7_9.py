sandwich_orders = ['Bauru', 'Pastrami', 'Bánh mì', 'Shawarma', 'Pastrami', 
                   'Katsu Sando', 'BLT', 'Croque Madame', 'Falafel', 'Cemita',
                   'Pastrami', 'Choripán']
finished_sandwiches =[]

print('We\'re out of pastrami.\n')

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami') 

while sandwich_orders:
    sandwich_ready = sandwich_orders.pop(0)
    print(f"Your {sandwich_ready} is ready!")
    finished_sandwiches.append(sandwich_ready)

print()

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
