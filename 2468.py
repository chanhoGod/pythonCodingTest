from collections import deque
N = int(input())

O = [[-1] * (N+1) for _ in range(N+1)]
visited = [[False] * (N+1) for _ in range(N+1)]
maxnum = 0

for i in range(1, N+1):
    A = list(map(int, input().split()))
    O[i] = [-1] + A
    if maxnum < max(A):
        maxnum = max(A)

def bfs(O, x, y, value):
    A = deque()
    A.append((x, y))
    
    areaTF = False
    while len(A) > 0:
        a, b = A.popleft()
        
        idx = O[a][b]
        if idx > value:
            if visited[a][b] == False:
                visited[a][b] = True
                areaTF = True
                
                if a > 0:
                    A.append((a-1, b))
                
                if b > 0:
                    A.append((a, b-1))
                    
                if a < N:
                    A.append((a+1, b))
                
                if b < N:
                    A.append((a, b+1))
    
    return areaTF
resultlist = list()
for k in range(0, maxnum+1):
    result = 0
    visited = [[False] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            if visited[i][j] == False:
                if bfs(O, i, j, k):
                    result += 1
    resultlist.append(result)

print(max(resultlist))