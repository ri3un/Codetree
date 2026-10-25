A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

if A1 > B1:
    print("A")
elif B1 > A1:
    print("B")
else:
    pass

if A1 == B1 and A2 > B2:
    print("A")
elif A1 == B1 and B2 > A2:
    print("B")
else:
    pass