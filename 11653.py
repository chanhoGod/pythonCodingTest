N = int(input())

A = 2

while N > 1:
    
    if N % A == 0:
        print(A)
        N = N // A
    elif N % A != 0:
        A += 1
    