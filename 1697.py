from collections import deque

N, K = map(int, input().split())
queue = deque()
queue.append((N, 0))
visited = [False] * 100001

while queue:
    a, cnt = queue.popleft()
    visited[a] = True
    if a == K:
        print(cnt)
        break
    
    if a > 0 and not visited[a-1]:
        visited[a-1] = True
        queue.append((a-1, cnt+1))
    if a+1 < 100001 and not visited[a+1]:
        visited[a+1] = True
        queue.append((a+1, cnt+1))
    if a*2 < 100001 and not visited[a*2]:
        visited[a*2] = True
        queue.append((a*2, cnt+1))