N, P, Q = map(int, input().split())

A = dict()
A[0] = 1

def recursion(n, p, q):
    if n in A:
        return A[n]
    
    A[n] = recursion(n // p, p, q) + recursion(n // q, p, q)
    return A[n]

print(recursion(N, P, Q))