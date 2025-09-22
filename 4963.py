import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(x, y, cnt):
    if O[x][y] == 1:
        visited[x][y] = True
    
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        nx, ny = x + dx, y + dy
        if h > nx >= 0 and w > ny >= 0 and not visited[nx][ny] and O[nx][ny] == 1:
            dfs(nx, ny, 1)
    
    return 1
        

while True:
    w, h = map(int, read().split())

    if w == 0 and h == 0:
        break
    
    O = [list(map(int, read().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)] 
    
    result = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and O[i][j] == 1:
                result += dfs(i, j, 0)
    print(result)
    