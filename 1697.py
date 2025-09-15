from collections import deque

N, K = map(int, input().split())
queue = deque()
queue.append((N, 0))
visited = [False] * 100001

while queue:
    p, t = queue.popleft()
    
    if p == K:
        print(t)
        break
    
    if p + 1 < 100001 and not visited[p+1]:
        visited[p+1] = True
        queue.append((p+1, t+1))
    
    if p - 1 >= 0 and not visited[p-1]:
        visited[p-1] = True
        queue.append((p-1, t+1))
    
    if p * 2 < 100001 and not visited[p*2]:
        visited[p*2] = True
        queue.append((p*2, t+1))
