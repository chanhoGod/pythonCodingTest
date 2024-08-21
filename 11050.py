from functools import reduce 

def get_factorial(N):
    if N == 0:
        N = 1
    
    A = reduce(lambda x, y : x * y, range(1, N+1))
    
    return A


N, K = map(int, input().split())

print(int(get_factorial(N) / (get_factorial(K) * get_factorial(N - K))))