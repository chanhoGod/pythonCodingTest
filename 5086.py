
while True:
    A, B = map(int, input().split(sep=" "))
    
    if A == 0 and B == 0:
        break
    
    if B % A == 0:
        print("factor")
        continue
    elif A % B == 0:
        print("multiple")
        continue
    else:
        print("neither")
        continue
    
    