N = int(input())
 
i = 1

while i <= N:
    a = int(input())
    if a % 3 == 0 and a % 2 == 1:
        print(a)
    else:
        pass
    i += 1