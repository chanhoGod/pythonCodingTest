import sys
from queue import PriorityQueue

read = sys.stdin.readline

A, B = map(int, read().strip().split())

N, M = map(int, read().strip().split())

R = [sys.maxsize for i in range(N + 1)]
O = [[] for i in range(N + 1)]
visited = [False] * (N + 1)
Q = PriorityQueue()

for i in range(M):
    idx1, idx2 = map(int, read().strip().split())

    O[idx1].append((idx2, 1))
    O[idx2].append((idx1, 1))

Q.put((1, A))
R[A] = 0


while Q.qsize() > 0:
    item = Q.get()
    start = item[1]
    
    if visited[start]:
        continue
    
    visited[start] = True
    
    for i in O[start]:
        end = i[0]
        R[end] = min(R[end], R[start] + 1)
        Q.put((1, end))

if R[B] > 10000:
    print(-1)
else:
    print(R[B])