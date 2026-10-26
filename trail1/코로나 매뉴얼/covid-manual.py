a1, b1 = input().split()
b1 = int(b1)
a2, b2 = input().split()
b2 = int(b2)
a3, b3 = input().split()
b3 = int(b3)

A = 0

if a1 == 'Y' and b1 >= 37:
    A += 1
else:
    pass

if a2 == 'Y' and b2 >= 37:
    A += 1
else:
    pass

if a3 == 'Y' and b3 >= 37:
    A += 1
else:
    pass

if A >= 2:
    print('E')
else:
    print('N')