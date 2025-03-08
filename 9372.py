import sys


read = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(read().strip())


def find(val):
    if O[val] != val:
        O[val] = find(O[val])
        return O[val]
    else:
        return val

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a != b:
        O[b] = a 
        C[b] = C[a] + 1

for _ in range(T):
    N, M = map(int, read().strip().split())
    
    O = [i for i in range(N+1)]
    C = [0 for i in range(N+1)]
    for i in range(M):
        a, b = map(int, read().strip().split())
        if find(a) != find(b):
            union(a, b)
    
    print(sum(C))
