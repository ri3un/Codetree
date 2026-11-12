i = 1

a = 0
b = 0

while i <= 10:
    N = int(input())
    i += 1

    if N % 3 == 0:
        a += 1
    if N % 5 == 0:
        b += 1
print(a, b)
