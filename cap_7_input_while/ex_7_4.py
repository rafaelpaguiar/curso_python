message = 'Inform your pizza toppings please.'
message += '\nType quit to exit.: '

topping = ''

while topping != 'quit':
    topping = input(message)
    if topping != 'quit':
        print(f'{topping.title()} is being added to the pizza.\n')
    else:
        print('Bye!')