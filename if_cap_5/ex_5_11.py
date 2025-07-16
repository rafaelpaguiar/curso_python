cardinals = [number for number in range(1,10)]

for cardinal in cardinals:
    if cardinal == 1:
        print(f"{cardinal}st.")
    elif cardinal == 2:
        print(f"{cardinal}nd.")
    elif cardinal == 3:
        print(f"{cardinal}rd.")
    else:
        print(f"{cardinal}th.")
