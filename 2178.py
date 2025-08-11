import sys
from collections import deque

read = sys.stdin.readline

N, M = map(int, read().split())

target_list = [list(map(int, read().strip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

target_queue = deque()
target_queue.append((0, 0, 1))
visited[0][0] = True
result = 1

while target_queue:
    x, y, cnt = target_queue.popleft()
    if x == N-1 and y == M-1:
        result = cnt
        break
    
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and target_list[nx][ny] == 1:
            visited[nx][ny] = True
            target_queue.append((nx, ny, cnt + 1))

print(result)