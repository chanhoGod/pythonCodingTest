import sys

sys.setrecursionlimit(10**6)
read = sys.stdin.readline

T = int(read().strip())

def dfs(val):
    if not visited[val]:
        visited[val] = True
        dfs(A[val])
        return 1
    else:
        return 1


for i in range(T):
    result = 0
    
    N = int(read().strip())
    O = [i for i in range(N+1)]
    A = [0] + list(map(int, read().split()))
    visited = [False] * (N+1)
    
    for j in range(1, N+1):
        if not visited[j]:
            result += dfs(j)
    
    print(result)

