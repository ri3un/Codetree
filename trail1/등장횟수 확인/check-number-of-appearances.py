cnt = 0
i = 1

while i <= 5:
    N = int(input())
    
    if N % 2 == 0:
        cnt += 1
    i += 1

print(cnt)