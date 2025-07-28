from random import choices

poll = [1,2,3,4,5,'a','b','c','d','e','f','g','h','i','k']
results = choices(poll,k=4)
print("Drawn numbers:", results)
my_billets = ['f',3,'c',6]
print("Your numbers:", my_billets)
count = 0

for result in results:
    for my_billet in my_billets:
        if my_billet == result:
            print("You won!")
        count += 1 

print("Looped:", count)