from collections import deque

N = int(input())
K = int(input())

O = [[] for _ in range(N+1)]
visited = [False] * (N+1) 

for i in range(K):
    a, b = map(int, input().split())
    
    O[a].append(b)
    O[b].append(a)

cnt = 0

def bfs(val):
    global cnt
    A = deque()
    A.append(val)
    visited[val] = True
    
    while len(A) > 0:
        a = A.popleft()
        
        for idx in O[a]:
            if visited[idx] == False:
                visited[idx] = True
                cnt += 1
                A.append(idx)

bfs(1)
print(cnt)