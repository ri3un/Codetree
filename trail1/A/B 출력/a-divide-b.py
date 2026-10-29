A, B = map(int, input().split())

print(A//B, end='.')

C = A % B

for i in range(20):
    C = C * 10
    print(C // B, end="")
    C = C % B