import sys
from collections import deque
read = sys.stdin.readline

T = int(read())
for _ in range(T):
    M, N, K = map(int, read().split())

    target_list = [[0] * N for _ in range(M)]
    target_queue = deque()
    visited = [[False] * N for _ in range(M)]

    for i in range(K):
        x, y = map(int, read().split())
        target_list[x][y] = 1

    result = 0
    for i in range(M):
        for j in range(N):
            if target_list[i][j] == 1 and visited[i][j] == False:
                target_queue.append((i, j))
                visited[i][j] = True
                
                while target_queue:
                    x, y = target_queue.popleft()
                    
                    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < M and 0 <= ny < N and target_list[nx][ny] == 1 and not visited[nx][ny]:
                            target_queue.append((nx, ny))
                            visited[nx][ny] = True
                result += 1
    print(result)