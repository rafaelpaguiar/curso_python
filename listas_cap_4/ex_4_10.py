cube = [number**3 for number in range(1,11)]

for number in cube:
    print(number)

print(f"Os três primeiros elementos da lista são {cube[:3]}")
print(f"Os três  elementos que ficam no meio da lista são {cube[4:7]}")
print(f"Os três últimos elementos da lista são {cube[-3:]}")