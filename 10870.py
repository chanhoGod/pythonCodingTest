def recursion(N):
    if N == 0:
        return N
    
    if N == 1:
        return N
    
    return recursion(N-1) + recursion(N-2)

N = int(input())

print(recursion(N))