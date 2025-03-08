import sys
from queue import PriorityQueue

read = sys.stdin.readline

N, M = map(int, read().strip().split())

O = [[] for i in range(N + 1)]
W = [sys.maxsize] * (N + 1)
visited = [False] * (N + 1)
Q = PriorityQueue()

for i in range(M):
    a, b, c = map(int, read().strip().split())
    O[a].append((b, c))
    O[b].append((a, c))

W[1] = 0
Q.put((0, 1))


while Q.qsize() > 0:
    cost, node = Q.get()
    
    if visited[node]:
        continue
    
    visited[node] = True
    for i in O[node]:
        next_node, next_cost = i
        
        if W[next_node] > W[node] + next_cost:
            W[next_node] = W[node] + next_cost
            Q.put((W[next_node], next_node))

print(W[N])