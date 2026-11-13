n = int(input())

sum_val = 0
i = 1

while i <= n:
    num = int(input())
    if num % 2 == 1 and num % 3 == 0:
        sum_val += num

    i += 1
print(sum_val)