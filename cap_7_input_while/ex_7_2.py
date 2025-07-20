booking = input("How many places do you want to book?: ")
booking = int(booking)

if booking > 8:
    print("Sorry, you have to wait for a table.")
else:
    print("Here you go.")