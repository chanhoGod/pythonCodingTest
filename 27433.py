def recursion(N):
    if N == 0:
        return 1
    
    if N == 1:
        return N
    
    return N * recursion(N - 1)

N = int(input())

print(recursion(N))