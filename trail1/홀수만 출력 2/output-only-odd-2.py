B, A = map(int, input().split())

for i in range(B, A-1, -1):
    if B>=i and A <= i:
        if i % 2 == 1:
            print(i, end = " ")