import sys
from collections import deque

read = sys.stdin.readline

N, M = map(int, read().split())

tomato_list = [list(map(int, read().split())) for _ in range(M)]

tomato_queue = deque()
count = 1
for i in range(M):
    for j in range(N):
        if tomato_list[i][j] == 1:
            tomato_queue.append((i, j, 1))
            
while tomato_queue:
    x, y, cnt = tomato_queue.popleft()
    
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and tomato_list[nx][ny] == 0:
            tomato_list[nx][ny] = 1
            tomato_queue.append((nx, ny, cnt + 1))
    
    count = max(count, cnt)

for i in range(M):
    if 0 in tomato_list[i]:
        print(-1)
        exit()
print(count-1)
