N = int(input())

sum_val = 0
i = 1
for i in range(i, N):
    if N % i == 0:
        sum_val += i
    else:
        pass

if N == sum_val:
    print('P')
else:
    print('N')