sum_val = 0
cnt = 0
i = 1
while i <= 10:
    N = int(input())

    if N >= 0 and N <= 200:
        sum_val += N
        cnt += 1
    i += 1
print(f"{sum_val} {sum_val/cnt:.1f}")
