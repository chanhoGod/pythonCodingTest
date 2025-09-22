import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M = map(int, read().split())

O = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, read().split())
    
    O[a].append(b)
    O[b].append(a)

visited = [False] * (N+1)

def dfs(idx) -> int:
    visited[idx] = True
    for i in O[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
    
    return 1
result = 0
for i in range(1, N+1):
    if not visited[i]:
        result += dfs(i)

print(result)