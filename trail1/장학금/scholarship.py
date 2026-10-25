score, p = map(int,input().split())



if score >= 90:
  
    if p >= 95:
        print(100000)

    elif p >= 90:
        print(50000)
    
    else:
        print(0)
else:
    print(0)