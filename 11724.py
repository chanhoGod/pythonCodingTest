import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, read().split())

target_list = [[] for _ in range(N+1)]

for i in range(M):
    x, y = map(int, read().split())
    target_list[x].append(y)
    target_list[y].append(x)

visited = [False] * (N+1)
visited[0] = True  # 0번 인덱스는 사용하지 않음
result = 0

def dfs(start, visited):
    
    visited[start] = True
    
    for i in target_list[start]:
        if not visited[i]:
            dfs(i, visited)
        

for i in range(1, N+1):
    if not visited[i]:
        dfs(i, visited)
        result += 1

print(result)