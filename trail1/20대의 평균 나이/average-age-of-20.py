sum_val = 0
cnt = 0
while True:
    n = int(input())

    if 20<= n <= 29:
        sum_val += n
        cnt += 1

    else:
        break
    
print(f"{sum_val / cnt:.2f}")