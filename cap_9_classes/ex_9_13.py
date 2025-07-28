from random import randint

class Dice:
    def __init__(self,sides):
        self.sides = sides
    
    def roll_dice(self):
        return randint(1,self.sides)

six_sided = Dice(6)

for roll in range(1,11):
    print(six_sided.roll_dice())

print("----------------")
ten_sided = Dice(10)

for roll in range(1,11):
    print(ten_sided.roll_dice())

print("----------------")
twenty_sided = Dice(20)

for roll in range(1,11):
    print(twenty_sided.roll_dice())