import sys
from collections import deque
read = sys.stdin.readline

N, M = map(int, read().split())
O = [list(map(int, read().strip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

queue = deque()
queue.append((0, 0, 1))
result = 1

while queue:
    x, y, d = queue.popleft()
    visited[x][y] = True
    if x == N-1 and y == M-1:
        result = d
        break
    
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and O[nx][ny] == 1:
            visited[nx][ny] = True
            queue.append((nx, ny, d+1))
    
    result = max(result, d)
    
print(result)