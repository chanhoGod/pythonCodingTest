import sys
N = int(input())

O = [[0] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)
result = sys.maxsize
for i in range(1, N+1):
    A = list(map(int, input().split()))
    
    O[i] = [0] + A

# dfs를 통한 백트래킹 구현
def dfs(val, first, cost, visited, depth):
    global result
    
    if depth == N:
        if O[val][first] != 0:
            result = min(result, cost+O[val][first])
        return
    
    if cost >= result:
        return    
    
    for i in range(1, N+1):
        if visited[i] == False and O[val][i] != 0:
            visited[i] = True
            dfs(i, first, cost + O[val][i], visited, depth+1)
            visited[i] = False
                
for i in range(1, N+1):
    visited = [False] * (N+1)
    visited[i] = True
    dfs(i, i, 0, visited, 1)

print(result)