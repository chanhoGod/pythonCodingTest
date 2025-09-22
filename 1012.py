import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(read())

def dfs(x, y):
    if visited[x][y]:
        return False
    
    visited[x][y] = True
    next = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for dx, dy in next:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and O[nx][ny] == 1:
            dfs(nx, ny)
        

for _ in range(T):
    
    M, N, K = map(int, read().split())
    O = [[0] * M for _ in range(N)]
    visited = [[True] * M for _ in range(N)]
    for i in range(K):
        a, b = map(int, read().split())
        O[b][a] = 1
        visited[b][a] = False
    
    result = 0
    for i in range(N):
        for j in range(M):
            if O[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                result += 1
    print(result)