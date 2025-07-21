active = True

message = 'Type your age to know the price of your ticket'
message += '\nType quit anytime to exit.'

print (message)

while active:
    age = input('Type your age please.: ')
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print('Your ticket is free.\n')
    elif age <=12:
            print('Your ticket is $10.\n')
    else:
         print('Your ticket is $15.\n')