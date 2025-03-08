import queue, sys

M, N = map(int, input().split())

O = [[] for i in range(N)]
visited = [[False for i in range(M)] for j in range(N)]
Q = queue.Queue()

def bfs():
    while Q.qsize() > 0:
        x, y, d = Q.get()
        # 아래 방향
        if x+1 < N: 
            if not visited[x+1][y] and O[x+1][y] != -1:
                visited[x+1][y] = True
                O[x+1][y] = d+1
                Q.put((x+1, y, d+1))
            
        # 위 방향
        if x-1 >= 0: 
            if not visited[x-1][y] and O[x-1][y] != -1:
                visited[x-1][y] = True
                O[x-1][y] = d+1
                Q.put((x-1, y, d+1))
            
        # 오른쪽 방향
        if y+1 < M: 
            if not visited[x][y+1] and O[x][y+1] != -1:
                visited[x][y+1] = True
                O[x][y+1] = d+1
                Q.put((x, y+1, d+1))
            
        # 왼쪽 방향
        if y-1 >= 0: 
            if not visited[x][y-1] and O[x][y-1] != -1:
                visited[x][y-1] = True
                O[x][y-1] = d+1
                Q.put((x, y-1, d+1))
            
for i in range(N):
    O[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(M):
        if O[i][j] == 1:
            Q.put((i, j, 1))
            visited[i][j] = True

bfs()
max_d = 0

for i in range(N):
    for j in range(M):
        if O[i][j] == 0:
            print(-1)
            sys.exit()
        max_d = max(max_d, O[i][j])

print(max_d - 1)