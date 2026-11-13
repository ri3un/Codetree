N = int(input())

cnt = 0
i = 0

for i in range(1, N+1):
    if i % 4 == 0:
        cnt += 1
    else:
        pass
    if i % 100 == 0 and i % 400 != 0:
        cnt -= 1

print(cnt)