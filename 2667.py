import sys
from collections import deque

read = sys.stdin.readline

N = int(read())

N_list = [[int(i) for i in read().strip()] for _ in range(N)]
visited = [[False] * N for i in range(N)]

dq = deque()
result = 0
result_list = []

for i in range(N):
    for j in range(N):
        if visited[i][j] == False and N_list[i][j] == 1:
            count = 1
            dq.append((i, j))
            visited[i][j] = True
            while dq:
                x, y = dq.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and N_list[nx][ny] == 1:
                        visited[nx][ny] = True
                        dq.append((nx, ny))
                        count += 1
            result += 1
            result_list.append(count)
            
print(result)
print(*sorted(result_list), sep='\n')