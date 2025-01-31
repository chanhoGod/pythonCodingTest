import sys
from collections import deque
read = sys.stdin.readline

# 상하좌우
px = [1, -1, 0, 0]
py = [0, 0, -1, 1]

N, M = map(int, read().split())

O = [[0] * M for i in range(N)]

for i in range(N):
    idx = list(input())
    for j in range(M):
        O[i][j] = int(idx[j])

visit_graph = [[False] * M for _ in range(N)] 


def bfs(x, y):
    
    queue = deque()
    queue.append((x, y))
    
    visit_graph[x][y] = True
    
    while queue:
        now = queue.popleft()
        
        for i in range(4):
            dx = now[0] + px[i]
            dy = now[1] + py[i]
            
            if dx >= 0 and dy >= 0 and dx < N and dy < M:
                if O[dx][dy] != 0 and visit_graph[dx][dy] != True:
                    visit_graph[dx][dy] = True
                    O[dx][dy] = O[now[0]][now[1]] + 1
                    queue.append((dx, dy))
                


bfs(0, 0)
print(O[N-1][M-1])