N = int(input())
sum_val = 0
i = 1

while i <= N:
    num = int(input())

    sum_val += num

    i += 1

print(sum_val, f"{sum_val/N:.1f}")
