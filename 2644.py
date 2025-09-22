import sys
from collections import deque
read = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())

M = int(input())
O = dict()
for i in range(M):
    x, y = map(int, input().split())
    if x not in O:
        O[x] = [y]
    else:
        O[x].append(y)
    
    if y not in O:
        O[y] = [x]
    else:
        O[y].append(x)
visited = [False] * (N+1)
queue = deque()
queue.append((A, 0))

while queue:
    idx, time = queue.popleft()
    if idx == B:
        print(time)
        exit()
    
    if idx in O:
        for i in O[idx]:
            if not visited[i]:
                visited[i] = True
                queue.append((i, time + 1))
    
print(-1)