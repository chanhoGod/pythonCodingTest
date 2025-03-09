import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(read().strip())

O = [[] for i in range(N+1)]
R = [0 for i in range(N+1)]
visited = [False] * (N+1)

# 트리 문제는 dfs를 써야 한다네용.

for i in range(N-1):
    a, b = map(int, read().strip().split())
    O[b].append(a)
    O[a].append(b)

visited[1] = True

def dfs(val):
    for i in O[val]:
        if not visited[i]:
            visited[i] = True
            R[i] = val
            dfs(i)

dfs(1)

for i in range(2, N+1):
    print(R[i])