import sys
from queue import PriorityQueue

read = sys.stdin.readline

V, E = map(int, read().strip().split())

K = int(read().strip())

O = [[] for i in range(V + 1)]
Q = PriorityQueue()

# 거리 리스트 초기화
W = [sys.maxsize for i in range(V+1)]
visited = [False for i in range(V+1)]
W[K] = 0

for i in range(E):
    u, v, w = map(int, read().strip().split())    
    O[u].append((v, w))

Q.put((0, K))

#update list
while Q.qsize() >= 1:
    item = Q.get()
    node = item[1]
    
    if not visited[node]:
        visited[node] = True
        for i in O[node]:
            vector = i[0]
            weight = i[1]
            if W[vector] > W[node] + weight:
                W[vector] = W[node] + weight
                Q.put((W[vector], vector))
    else:
        continue

for i in range(1, V + 1):
    if visited[i]:
        print(W[i])
    else:
        print("INF")