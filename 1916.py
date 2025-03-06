import sys
from queue import PriorityQueue

read = sys.stdin.readline

N = int(read().strip())
M = int(read().strip())

O = [[] for i in range(N+1)]
W = [sys.maxsize] * (N+1)
visited = [False] * (N+1)
Q = PriorityQueue()

for i in range(M):
    start, end, value = map(int, read().strip().split())
    O[start].append((end, value))

start_city, end_city = map(int, read().strip().split())

W[start_city] = 0
Q.put((0, start_city))

while Q.qsize() > 0:
    item = Q.get()
    start = item[1]
    
    if visited[start]:
        continue
    
    visited[start] = True
    for i in O[start]:
        end = i[0]
        value = i[1]
        
        if W[end] > W[start] + value:
            W[end] = W[start] + value
            Q.put((W[end], end))
    
print(W[end_city])