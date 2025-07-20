print('car' == 'car')
print('car' == 'CaR')
print('car' != 'car')
print('car' != 'CaR')
print('car' == 'CaR'.lower())
print(10 == 10)
print(10 != 10)
print(10 < 1)
print(10 > 1)
print(5 <= 1)
print(5 >= 1)
print(4 > 3 and 3 > 2)
print(4 > 3 and 3 > 5)
print(4 > 3 or 3 > 2)
print(4 > 3 or 3 > 5)
print(4 < 3 or 3 < 2)

list = [number*2 for number in range(1,10)]
print(8 in list)
list = [number*2 for number in range(1,10)]
print(8 not in list)

list = [number*2 for number in range(1,10)]
print(7 in list)
list = [number*2 for number in range(1,10)]
print(7 not in list)
